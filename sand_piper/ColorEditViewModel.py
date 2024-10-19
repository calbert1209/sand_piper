from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent, EncoderSwitchEvent

PREFIX = "   "
SELECTED = " > "


class RGBValue:
    def __init__(self, r: int, g: int, b: int) -> None:
        self._r = r
        self._g = g
        self._b = b

    def __clamp__(self, value: int):
        return max(0, min(value, 255))

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value: int):
        self._r = self.__clamp__(value)

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value: int):
        self._g = self.__clamp__(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value: int):
        self._b = self.__clamp__(value)

    @property
    def hexaDecimalString(self):
        return f"{self._r:02x}{self._g:02x}{self._b:02x}"

    @property
    def hexValue(self):
        return int(self.hexaDecimalString, 16)


class ColorEditViewModel:
    def __init__(self, eventBus: EventBus, initialRgb: tuple[int, int, int]) -> None:
        eventBus.addEventListener("key_down", self.__onKeyDown)
        eventBus.addEventListener("enc_change", self.__onEncoderChange)
        self._eventBus = eventBus
        self._options = ["r", "g", "b"]
        self._optionIndex = 0
        (r, g, b) = initialRgb
        self._value = RGBValue(r, g, b)

    def __onKeyDown(self, event: KeyEvent):

        if event.key_number < 3:
            self._optionIndex = event.key_number
        if event.key_number == 9:
            print("no change")
        if event.key_number == 11:
            print(f"next value: {self._value.hexaDecimalString}")

    def __onEncoderChange(self, event: EncoderEvent):
        delta = event.delta
        if self._optionIndex == 0:
            nextValue = self._value.r + delta
            self.setRed(nextValue)

        elif self._optionIndex == 1:
            nextValue = self._value.g + delta
            self.setGreen(nextValue)

        elif self._optionIndex == 2:
            nextValue = self._value.b + delta
            self.setBlue(nextValue)

    def setRed(self, value: int):
        self._value.r = value

    def setGreen(self, value: int):
        self._value.g = value

    def setBlue(self, value: int):
        self._value.b = value

    @property
    def redValue(self):
        return f"{self._value.r:03}"

    @property
    def greenValue(self):
        return f"{self._value.g:03}"

    @property
    def blueValue(self):
        return f"{self._value.b:03}"

    @property
    def rHeader(self):
        if self._optionIndex == 0:
            return "[R]"
        return " R "

    @property
    def gHeader(self):
        if self._optionIndex == 1:
            return "[G]"
        return " G "

    @property
    def bHeader(self):
        if self._optionIndex == 2:
            return "[B]"
        return " B "

    def valueString(self):
        return self._value.hexaDecimalString

    @property
    def hexValue(self):
        return self._value.hexValue
