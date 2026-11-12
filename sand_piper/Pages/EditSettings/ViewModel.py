from adafruit_macropad import MacroPad
from sand_piper.Models.Model import KeySettings
from sand_piper.Pages.EditSettings.Display import EditSettingsDisplay
from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent

OPTIONS = ["label", "color", "keyCodes"]


class EditSettingsViewModel:
    _scrollIndex = 1
    _optionIndex = 0
    _active = 0x333333
    _activeOrange = 0xee4400
    _dimOrange = 0x160800
    _focusOrange = 0xaa3300
    _dimRed = 0x330000
    _activeRed = 0xdd0000
    _dimGreen = 0x003300
    _activeGreen = 0x00dd00
    _noLight = 0x000000

    def __init__(self, view: EditSettingsDisplay, initialValue: KeySettings, onComplete, title: str = "SETTINGS"):
        self._view = view
        self._value = initialValue
        self._onComplete = onComplete
        self._title = title

    def __onKeyDown(self, event: KeyEvent):

        if event.key_number == 0:
            self._pixels[0] = self._activeOrange
            self._optionIndex = 0

        if event.key_number == 3:
            self._pixels[3] = self._activeOrange
            self._optionIndex = 1

        if event.key_number == 6:
            self._pixels[6] = self._activeOrange
            self._optionIndex = 2

        if event.key_number == 9:
            self._pixels[9] = self._activeRed
            self._onComplete(None)

        if event.key_number == 11:
            self._pixels[11] = self._activeGreen
            option = OPTIONS[self._optionIndex]
            self._onComplete(option)
        self._pixels.show()

    def __onKeyUp(self, event: KeyEvent):
        for i in range(3):
            pixelIndex = i * 3
            color = self._focusOrange if self._optionIndex == i else self._dimOrange
            self._pixels[pixelIndex] = color

        if event.key_number == 9:
            self._pixels[9] = self._dimRed

        if event.key_number == 11:
            self._pixels[11] = self._dimGreen

        self._pixels.show()

    def __onEncChange(self, event: EncoderEvent):
        pass

    @property
    def _valueString(self):
        return "value string..."

    def __updateView(self):
        self._view.setTitle(self._title)
        labelKey = "> label" if self._optionIndex == 0 else "  label"
        labelValue = self._value.getSettingString("label")
        self._view.setText(0, f"{labelKey}: {labelValue}")
        colorKey = "> color" if self._optionIndex == 1 else "  color"
        colorValue = self._value.getSettingString("color")
        self._view.setText(1, f"{colorKey}: {colorValue}")
        codesKey = "> codes" if self._optionIndex == 2 else "  codes"
        codesValue = self._value.getSettingString("codes")
        self._view.setText(2, f"{codesKey}: {codesValue}",)
        self._view.show()

    def __updatePixels(self):
        pass

    def __initPixels(self):
        for i in range(3):
            pixelIndex = i * 3
            color = self._focusOrange if self._optionIndex == i else self._dimOrange
            self._pixels[pixelIndex] = color
        self._pixels[9] = self._dimRed
        self._pixels[11] = self._dimGreen
        self._pixels.show()

    def update(self):
        self.__updateView()
        self.__updatePixels()

    def connect(self, macroPad: MacroPad, eventBus: EventBus):
        macroPad.pixels.auto_write = False
        macroPad.pixels.brightness = 0.2
        macroPad.display.root_group = self._view.group
        self._pixels = macroPad.pixels
        self.__initPixels()
        eventBus.setOnKeyDown(self.__onKeyDown)
        eventBus.setOnKeyUp(self.__onKeyUp)
        eventBus.setOnEncChange(self.__onEncChange)

    def disconnect(self):
        self._pixels.fill(0x000000)
        self._pixels.show()
        self._pixels = None
