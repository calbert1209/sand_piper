class Prefix:
    """Enum-like class for the prefix of the serialized words"""

    SWORD = "#"
    WORD = "_"
    LWORD = "$"
    PCODE = "+"
    RCODE = "-"

    ARRAY = "*"
    COMM = "<"
    PAGE = "["

    END = "\n"


class ParsableAsBytes:
    @staticmethod
    def fromBytes(data: bytes) -> "ParsableAsBytes":
        raise NotImplementedError()

    def canParseFrom(data: bytes) -> bool:
        raise NotImplementedError()


class PushCode(ParsableAsBytes):
    _prefix = Prefix.PCODE
    length = 2
    value = 0

    def __init__(self, value: int) -> None:
        self.value = value

    def toBytes(self) -> bytes:
        return self._prefix.encode() + bytes([self.value])

    @staticmethod
    def fromBytes(data: bytes):
        return PushCode(int(data[1]))

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        if len(data) != PushCode.length:
            return False

        return data[0] == PushCode._prefix.encode()[0]


class ReleaseCode(ParsableAsBytes):
    _prefix = Prefix.RCODE
    length = 2
    value = 0

    def __init__(self, value: int) -> None:
        self.value = value

    def toBytes(self) -> bytes:
        return self._prefix.encode() + bytes([self.value])

    @staticmethod
    def fromBytes(data: bytes):
        return ReleaseCode(int(data[1]))

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        if len(data) != ReleaseCode.length:
            return False

        return data[0] == ReleaseCode._prefix.encode()[0]


class ShortWord(ParsableAsBytes):
    _prefix = Prefix.SWORD
    length = 4

    def __init__(self, value: bytes) -> None:
        self.value = value

    def toBytes(self) -> bytes:
        raw = bytes(self.value)[:3]
        if len(raw) < 3:
            raw = raw + b"\x00" * (3 - len(raw))
        return self._prefix.encode() + raw

    def toInts(self) -> list[int]:
        return [int(i) for i in self.value]

    @staticmethod
    def fromBytes(data: bytes):
        return ShortWord(data[1:])

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        if len(data) != ShortWord.length:
            return False

        return data[0] == ord(ShortWord._prefix)


class Word(ParsableAsBytes):
    _prefix = Prefix.WORD
    length = 8

    def __init__(self, value: bytes) -> None:
        if isinstance(value, str):
            value = value.encode()
        self.value = value

    def toBytes(self) -> bytes:
        text = self.toString()[:7]
        padded = f"{text:<7}".encode()[:7]
        return self._prefix.encode() + padded

    def toInts(self) -> list[int]:
        return [int(i) for i in self.value.split()]

    def toString(self) -> str:
        return self.value.decode()

    def toTrimmed(self) -> str:
        return self.toString().strip()

    @staticmethod
    def fromBytes(data: bytes):
        return Word(data[1:])

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        if len(data) != Word.length:
            return False

        return data[0] == ord(Word._prefix)


class LongWord(ParsableAsBytes):
    _prefix = Prefix.LWORD
    length = 16

    def __init__(self, value: bytes) -> None:
        if isinstance(value, str):
            value = value.encode()
        self.value = value

    def toBytes(self) -> bytes:
        text = self.toString()[:15]
        padded = f"{text:<15}".encode()[:15]
        return self._prefix.encode() + padded

    def toInts(self) -> list[int]:
        return [int(i) for i in self.value.split()]

    def toString(self) -> str:
        return self.value.decode()

    def toTrimmed(self) -> str:
        return self.toString().strip()

    @staticmethod
    def fromBytes(data: bytes):
        return LongWord(data[1:])

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        if len(data) != LongWord.length:
            return False

        return data[0] == ord(LongWord._prefix)


class ParsableBytesContainer:
    @staticmethod
    def fromBytes(data: bytes, decode) -> "ParsableAsBytes":
        raise NotImplementedError()

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        raise NotImplementedError()


def measureItemLength(data: bytes, offset: int = 0) -> int:
    if offset >= len(data):
        raise ValueError("Unexpected end of data while measuring item length")

    prefix = data[offset]
    if prefix == ord(Prefix.PCODE) or prefix == ord(Prefix.RCODE):
        return PushCode.length
    if prefix == ord(Prefix.SWORD):
        return ShortWord.length
    if prefix == ord(Prefix.WORD):
        return Word.length
    if prefix == ord(Prefix.LWORD):
        return LongWord.length
    if prefix == ord(Prefix.COMM):
        codesOffset = offset + 1 + Word.length + ShortWord.length
        return (codesOffset - offset) + measureItemLength(data, codesOffset)
    if prefix == ord(Prefix.PAGE):
        cmdsOffset = offset + 1 + LongWord.length
        return (cmdsOffset - offset) + measureItemLength(data, cmdsOffset)
    if prefix == ord(Prefix.ARRAY):
        if offset + 1 >= len(data):
            raise ValueError("Unexpected end of data in Array header")
        count = data[offset + 1]
        cursor = offset + 2
        for _ in range(count):
            cursor += measureItemLength(data, cursor)
        return cursor - offset

    raise ValueError(f"Unknown prefix byte: {prefix} at offset {offset}")


class Array(ParsableBytesContainer):
    _prefix = Prefix.ARRAY
    _items = None
    _length = -1

    def __init__(self, length: int, items: list) -> None:
        self._length = length
        self._items = items

    def toBytes(self) -> bytes:
        body = b"".join([item.toBytes() for item in self._items])
        return self._prefix.encode() + bytes([len(self._items)]) + body

    @staticmethod
    def __parseContents(contents: bytes, expectedLength=None) -> list[bytes]:
        if len(contents) == 0:
            return []
        output = []
        cursor = 0
        while cursor < len(contents):
            if expectedLength is not None and len(output) >= expectedLength:
                break
            itemLen = measureItemLength(contents, cursor)
            output.append(contents[cursor : cursor + itemLen])
            cursor += itemLen

        return output

    @property
    def length(self) -> int:
        return self._length

    @property
    def items(self) -> list[ParsableAsBytes]:
        return self._items

    @staticmethod
    def fromBytes(data: bytes, decode) -> "Array":
        length = data[1]
        contents = data[2:]
        items = [decode(item) for item in Array.__parseContents(contents, length)]
        if len(items) != length:
            print(f"items{len(items)} declared: {length}")
            raise ValueError("Array length does not match items' length")

        return Array(length=length, items=items)

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        return len(data) >= 2 and data[0] == ord(Array._prefix)


class KeyCommand(ParsableBytesContainer):
    _prefix = Prefix.COMM
    _label: Word
    _color: ShortWord
    _codes: Array

    def __init__(self, label, color, codes) -> None:
        self._label = label if isinstance(label, Word) else Word(str(label))
        if isinstance(color, ShortWord):
            self._color = color
        else:
            self._color = ShortWord(bytes(color))
        if isinstance(codes, Array):
            self._codes = codes
        else:
            self._codes = Array(len(codes), codes)

    def toBytes(self) -> bytes:
        return (
            self._prefix.encode()
            + self._label.toBytes()
            + self._color.toBytes()
            + self._codes.toBytes()
        )

    @property
    def label(self):
        return self._label

    @property
    def color(self):
        return self._color

    @property
    def codes(self):
        return self._codes

    @staticmethod
    def fromBytes(data: bytes, decode):
        colorStart = Word.length + 1
        keyCodesStart = colorStart + ShortWord.length
        label = decode(data[1:colorStart])
        color = decode(data[colorStart:keyCodesStart])
        codes = decode(data[keyCodesStart:])
        return KeyCommand(label, color, codes)

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        if len(data) < 1 + Word.length + ShortWord.length + 2:
            return False

        if data[0] != ord(KeyCommand._prefix):
            return False

        if data[1] != ord(Prefix.WORD):
            return False

        if data[1 + Word.length] != ord(Prefix.SWORD):
            return False

        if data[1 + Word.length + ShortWord.length] != ord(Prefix.ARRAY):
            return False

        return True


class PadPage(ParsableBytesContainer):
    _prefix = Prefix.PAGE

    def __init__(self, label, commands):
        self._label = label if isinstance(label, LongWord) else LongWord(str(label))
        if isinstance(commands, Array):
            self._commands = commands
        else:
            self._commands = Array(len(commands), commands)

    def toBytes(self) -> bytes:
        return (
            self._prefix.encode()
            + self._label.toBytes()
            + self._commands.toBytes()
        )

    @property
    def label(self):
        return self._label

    @property
    def commands(self):
        return self._commands

    @staticmethod
    def fromBytes(data: bytes, decode):
        labelStart = 1
        commandsStart = labelStart + LongWord.length
        label = decode(data[labelStart:commandsStart])
        commands = decode(data[commandsStart:])
        return PadPage(label, commands)

    @staticmethod
    def canParseFrom(data: bytes) -> bool:
        if len(data) < 1 + LongWord.length + 2:
            return False

        if data[0] != ord(PadPage._prefix):
            return False

        if data[1] != ord(Prefix.LWORD):
            return False

        if data[1 + LongWord.length] != ord(Prefix.ARRAY):
            return False

        return True


class Decoder:
    """Class to decode bytes into settings"""

    def __init__(
        self,
        fixedLengthClasses=None,
        containerClasses=None,
    ) -> None:
        self._fixedLengthClasses = (
            fixedLengthClasses
            if fixedLengthClasses is not None
            else [PushCode, ReleaseCode, ShortWord, Word, LongWord]
        )
        self._containerClasses = (
            containerClasses
            if containerClasses is not None
            else [Array, KeyCommand, PadPage]
        )

    def decode(self, data: bytes):
        for cls in self._fixedLengthClasses:
            if cls.canParseFrom(data):
                return cls.fromBytes(data)

        for cls in self._containerClasses:
            if cls.canParseFrom(data):
                return cls.fromBytes(data, self.decode)

        raise ValueError("Data cannot be parsed")

    def trim(self, nvmData: bytes) -> bytes:
        raw = bytes(nvmData[:])
        if len(raw) == 0:
            return b""
        try:
            rootLen = measureItemLength(raw, 0)
            if rootLen <= len(raw):
                return raw[:rootLen]
        except Exception:
            pass
        return raw.split(Prefix.END.encode())[0]


class Encoder:
    """Class to encode settings into bytes with END terminator"""

    @staticmethod
    def encode(item) -> bytes:
        return item.toBytes() + Prefix.END.encode()

