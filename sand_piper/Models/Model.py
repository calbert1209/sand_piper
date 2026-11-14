
from sand_piper.Models.Keycodes import KeyCode, KeyCodes
from sand_piper.Models.Mgogo import (
    Array,
    KeyCommand as MgogoKeyCommand,
    LongWord,
    PadPage,
    PushCode,
    ReleaseCode,
    ShortWord,
    Word,
)
from sand_piper.Models.RgbValue import RGBValue


class KeySettings:
    def __init__(self, label: str, color: RGBValue, keyCodes: list[KeyCode]) -> None:
        self._label = label
        self._color = color
        self._codes = keyCodes

    @staticmethod
    def empty() -> "KeySettings":
        return KeySettings(label="", color=RGBValue(0, 0, 0), keyCodes=[])

    @property
    def label(self) -> str:
        return self._label

    @property
    def color(self) -> RGBValue:
        return self._color

    @property
    def keyCodes(self) -> list[KeyCode]:
        return self._codes

    def getSetting(self, key):
        if key == "label":
            return self._label
        if key == "color":
            return self._color
        if key == "keyCodes" or key == "codes":
            return self._codes

        raise Exception(f"Invalid key: `{key}`")

    def getSettingString(self, key: str):
        if key == "label":
            return self._label
        if key == "color":
            return self._color.hexaDecimalString
        if key == "keyCodes" or key == "codes":
            return "".join([code.valueString for code in self._codes])

        raise Exception(f"Invalid key: `{key}`")

    def clone(self, **kwargs):
        label = kwargs.get('label', self._label)
        color = kwargs.get('color', self._color)
        codes = kwargs.get('keyCodes', self._codes)
        return KeySettings(label=label, color=color, keyCodes=codes)

    def toMgogo(self) -> MgogoKeyCommand:
        word = Word(self._label)
        sword = ShortWord(bytes([self._color.r, self._color.g, self._color.b]))
        mgogo_codes = [
            PushCode(c.value) if c.press else ReleaseCode(c.value)
            for c in self._codes
        ]
        return MgogoKeyCommand(word, sword, Array(len(mgogo_codes), mgogo_codes))

    @staticmethod
    def fromMgogo(cmd: MgogoKeyCommand) -> "KeySettings":
        label = cmd.label.toTrimmed()
        rgb = cmd.color.toInts()
        color = RGBValue(rgb[0], rgb[1], rgb[2])
        codes = []
        for item in cmd.codes.items:
            is_press = isinstance(item, PushCode)
            codes.append(KeyCodes.fromValue(item.value, press=is_press))
        return KeySettings(label=label, color=color, keyCodes=codes)


class ControlPage:
    def __init__(self, name: str, keys: list[KeySettings]) -> None:
        self.name = name
        self.keys = keys

    @staticmethod
    def empty(name: str) -> "ControlPage":
        keys = [
            KeySettings(label="", color=RGBValue(0, 0, 0), keyCodes=[])
            for _ in range(12)
        ]
        return ControlPage(name=name, keys=keys)

    def toMgogo(self) -> PadPage:
        lword = LongWord(self.name)
        cmds = [k.toMgogo() for k in self.keys]
        return PadPage(lword, Array(len(cmds), cmds))

    @staticmethod
    def fromMgogo(page: PadPage) -> "ControlPage":
        name = page.label.toTrimmed()
        keys = [KeySettings.fromMgogo(cmd) for cmd in page.commands.items]
        while len(keys) < 12:
            keys.append(KeySettings(label="", color=RGBValue(0, 0, 0), keyCodes=[]))
        return ControlPage(name=name, keys=keys[:12])

