from adafruit_macropad import MacroPad
from sand_piper.Models import RgbValue
from sand_piper.Pages.EditColor.Display import EditColorDisplay
from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent
from sand_piper.Models.RgbValue import RGBValue


class EditColorViewModel:
    _options = ["r", "g", "b"]
    _optionIndex = 0

    def __init__(self, view: EditColorDisplay, initialValue: RGBValue, onComplete) -> None:
        self._view = view
        self._value = RGBValue(initialValue.r, initialValue.g, initialValue.b)
        self.__onComplete = onComplete

    def __onKeyDown(self, event: KeyEvent):

        if event.key_number == 6:
            self._optionIndex = 0
        if event.key_number == 7:
            self._optionIndex = 1
        if event.key_number == 8:
            self._optionIndex = 2
        if event.key_number == 9:
            self.__onComplete(None)
        if event.key_number == 11:
            rgb = (self._value.r, self._value.g, self._value.b)
            self.__onComplete(rgb)

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

    def __updateView(self):
        self._view.setPrimaryLabel("OK")
        self._view.setText(0, self._asString(self._value.r))
        self._view.setText(1, self._asString(self._value.g))
        self._view.setText(2, self._asString(self._value.b))
        self._view.setText(3, self._rHeader)
        self._view.setText(4, self._gHeader)
        self._view.setText(5, self._bHeader)
        self._view.setTitle(self._value.hexaDecimalString)
        self._view.show()

    def __updatePixels(self):
        for i in range(6):
            self._pixels[i] = self.hexValue

        self._pixels[6] = 0xff0000
        self._pixels[7] = 0x00ff00
        self._pixels[8] = 0x0000ff
        self._pixels[9] = 0xff0000
        self._pixels[11] = 0x00ff00
        self._pixels.show()

    def update(self):
        self.__updateView()
        self.__updatePixels()

    def connect(self, eventBus: EventBus, macroPad: MacroPad):
        self._pixels = macroPad.pixels
        macroPad.pixels.auto_write = False
        macroPad.pixels.brightness = 0.2
        macroPad.display.root_group = self._view.group
        eventBus.setOnKeyDown(self.__onKeyDown)
        eventBus.setOnEncChange(self.__onEncoderChange)

    def disconnect(self):
        self._pixels.fill(0x000000)
        self._pixels.show()
        self._pixels = None
