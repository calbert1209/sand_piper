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
        self._initialValue = RGBValue(r, g, b)
        self._value = RGBValue(r, g, b)

    def __onKeyDown(self, event: KeyEvent):

        if event.key_number == 0:
            self._optionIndex = 0
        if event.key_number == 3:
            self._optionIndex = 1
        if event.key_number == 6:
            self._optionIndex = 2
        if event.key_number == 9:
            print(f"no change: {self._initialValue.hexaDecimalString}")
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
        prefix = PREFIX
        if self._optionIndex == 0:
            prefix = SELECTED
        return f"{prefix}r: {self._value.r}"

    @property
    def greenValue(self):
        prefix = PREFIX
        if self._optionIndex == 1:
            prefix = SELECTED
        return f"{prefix}g: {self._value.g}"

    @property
    def blueValue(self):
        prefix = PREFIX
        if self._optionIndex == 2:
            prefix = SELECTED
        return f"{prefix}b: {self._value.b}"

    def valueString(self):
        return self._value.hexaDecimalString

    @property
    def hexValue(self):
        return self._value.hexValue
