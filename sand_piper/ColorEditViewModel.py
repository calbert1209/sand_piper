from adafruit_macropad import _PixelMapLite as PixelMap
from sand_piper.EditColorDisplay import Display
from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent, EncoderSwitchEvent
from sand_piper.RgbValue import RGBValue


class ColorEditViewModel:
    def __init__(self, eventBus: EventBus, view: Display, pixels: PixelMap, initialRgb: tuple[int, int, int]) -> None:
        eventBus.addEventListener("key_down", self.__onKeyDown)
        eventBus.addEventListener("enc_change", self.__onEncoderChange)
        self._eventBus = eventBus
        self._view = view
        self._pixels = pixels
        self._pixels.auto_write = False
        self._pixels.brightness = 0.2
        self._options = ["r", "g", "b"]
        self._optionIndex = 0
        (r, g, b) = initialRgb
        self._value = RGBValue(r, g, b)

    def __onKeyDown(self, event: KeyEvent):

        if event.key_number == 6:
            self._optionIndex = 0
        if event.key_number == 7:
            self._optionIndex = 1
        if event.key_number == 8:
            self._optionIndex = 2
        if event.key_number == 9:
            print("no change")
        if event.key_number == 11:
            print(f"next value: {self._value.hexaDecimalString}")

    def __onEncoderChange(self, event: EncoderEvent):
        delta = event.delta
        if self._optionIndex == 0:
            nextValue = self._value.r + delta
            self._value.r = nextValue

        elif self._optionIndex == 1:
            nextValue = self._value.g + delta
            self._value.g = nextValue

        elif self._optionIndex == 2:
            nextValue = self._value.b + delta
            self._value.b = nextValue

    def _asString(self, value: int):
        return f"{value:03}"

    @property
    def _rHeader(self):
        if self._optionIndex == 0:
            return "[R]"
        return " R "

    @property
    def _gHeader(self):
        if self._optionIndex == 1:
            return "[G]"
        return " G "

    @property
    def _bHeader(self):
        if self._optionIndex == 2:
            return "[B]"
        return " B "

    @property
    def hexValue(self):
        return self._value.hexValue

    def _updateView(self):
        self._view.setPrimaryLabel("OK")
        self._view.setSecondaryLabel("X")
        self._view.setText(3, self._rHeader)
        self._view.setText(4, self._gHeader)
        self._view.setText(5, self._bHeader)
        self._view.setText(0, self._asString(self._value.r))
        self._view.setText(1, self._asString(self._value.g))
        self._view.setText(2, self._asString(self._value.b))
        self._view.setTitle(self._value.hexaDecimalString)
        self._view.show()

    def _updatePixels(self):
        for i in range(6):
            self._pixels[i] = self.hexValue

        self._pixels[6] = 0xff0000
        self._pixels[7] = 0x00ff00
        self._pixels[8] = 0x0000ff
        self._pixels[9] = 0xff0000
        self._pixels[11] = 0x00ff00
        self._pixels.show()

    def update(self):
        self._updateView()
        self._updatePixels()
