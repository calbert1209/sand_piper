from adafruit_macropad import MacroPad
from sand_piper.Pages.EditColor.Display import EditColorDisplay
from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent, EncoderSwitchEvent
from sand_piper.Models.RgbValue import RGBValue


class EditColorViewModel:
    _dimRed = 0x330000
    _activeRed = 0xDD0000
    _dimGreen = 0x003300
    _activeGreen = 0x00DD00
    _noLight = 0x000000

    def __init__(self, view: EditColorDisplay, initialValue: RGBValue, onComplete) -> None:
        self._view = view
        self._value = RGBValue(initialValue.r, initialValue.g, initialValue.b)
        self.__onComplete = onComplete
        self._optionIndex = 0
        self._coarseMode = True
        self._pixels = None

    @property
    def stepSize(self) -> int:
        return 16 if self._coarseMode else 1

    def __onKeyDown(self, event: KeyEvent):
        if event.key_number == 6:
            self._optionIndex = 0
        elif event.key_number == 7:
            self._optionIndex = 1
        elif event.key_number == 8:
            self._optionIndex = 2
        elif event.key_number == 9:
            self._pixels[9] = self._activeRed
            self._pixels.show()
            self.__onComplete(None)
            return
        elif event.key_number == 11:
            self._pixels[11] = self._activeGreen
            self._pixels.show()
            rgb = (self._value.r, self._value.g, self._value.b)
            self.__onComplete(rgb)
            return

        self.__updateView()
        self.__updatePixels()

    def __onKeyUp(self, event: KeyEvent):
        self.__updateView()
        self.__updatePixels()

    def __onEncoderChange(self, event: EncoderEvent):
        delta = event.delta * self.stepSize
        if self._optionIndex == 0:
            self._value.r = self._value.r + delta
        elif self._optionIndex == 1:
            self._value.g = self._value.g + delta
        elif self._optionIndex == 2:
            self._value.b = self._value.b + delta

        self.__updateView()
        self.__updatePixels()

    def __onEncSwitchDown(self, event: EncoderSwitchEvent):
        self._coarseMode = not self._coarseMode
        self.__updateView()
        self.__updatePixels()

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
        self._view.setPrimaryLabel("SAVE")
        self._view.setText(0, self._asString(self._value.r))
        self._view.setText(1, self._asString(self._value.g))
        self._view.setText(2, self._asString(self._value.b))
        self._view.setText(3, self._rHeader)
        self._view.setText(4, self._gHeader)
        self._view.setText(5, self._bHeader)
        self._view.setTitle(f"#{self._value.hexaDecimalString.upper()} [x{self.stepSize}]")
        self._view.show()

    def __updatePixels(self):
        for i in range(6):
            self._pixels[i] = self.hexValue

        self._pixels[6] = 0xFF0000 if self._optionIndex == 0 else 0x220000
        self._pixels[7] = 0x00FF00 if self._optionIndex == 1 else 0x002200
        self._pixels[8] = 0x0000FF if self._optionIndex == 2 else 0x000022
        self._pixels[9] = self._dimRed
        self._pixels[10] = self._noLight
        self._pixels[11] = self._dimGreen
        self._pixels.show()

    def update(self):
        pass

    def connect(self, macroPad: MacroPad, eventBus: EventBus):
        self._pixels = macroPad.pixels
        macroPad.pixels.auto_write = False
        macroPad.pixels.brightness = 0.2
        macroPad.display.root_group = self._view.group
        self.__updateView()
        self.__updatePixels()
        eventBus.setOnKeyDown(self.__onKeyDown)
        eventBus.setOnKeyUp(self.__onKeyUp)
        eventBus.setOnEncChange(self.__onEncoderChange)
        eventBus.setOnEncSwitchDown(self.__onEncSwitchDown)

    def disconnect(self):
        self._pixels.fill(0x000000)
        self._pixels.show()
        self._pixels = None
