from adafruit_macropad import MacroPad
from sand_piper.Models.Model import KeySettings
from sand_piper.Pages.EditSettings.Display import EditSettingsDisplay
from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent

OPTIONS = ["label", "color", "keyCodes"]


def _truncate(text: str, maxLen: int = 21) -> str:
    if len(text) > maxLen:
        return text[:maxLen - 2] + ".."
    return text


class EditSettingsViewModel:
    _dimOrange = 0x160800
    _focusOrange = 0xAA3300
    _activeOrange = 0xEE4400
    _dimRed = 0x330000
    _activeRed = 0xDD0000
    _dimYellow = 0x332200
    _activeYellow = 0xDDAA00
    _dimGreen = 0x003300
    _activeGreen = 0x00DD00

    def __init__(self, view: EditSettingsDisplay, initialValue: KeySettings, onComplete, title: str = "SETTINGS"):
        self._view = view
        self._value = initialValue
        self._onComplete = onComplete
        self._title = title
        self._optionIndex = 0
        self._pixels = None

    def __onKeyDown(self, event: KeyEvent):
        if event.key_number == 0:
            self._optionIndex = 0
            self._pixels[0] = self._activeOrange
            self._pixels.show()
            self._onComplete(OPTIONS[0])
            return

        if event.key_number == 3:
            self._optionIndex = 1
            self._pixels[3] = self._activeOrange
            self._pixels.show()
            self._onComplete(OPTIONS[1])
            return

        if event.key_number == 6:
            self._optionIndex = 2
            self._pixels[6] = self._activeOrange
            self._pixels.show()
            self._onComplete(OPTIONS[2])
            return

        if event.key_number == 9:
            self._pixels[9] = self._activeRed
            self._pixels.show()
            self._onComplete(None)
            return

        if event.key_number == 10:
            self._pixels[10] = self._activeYellow
            self._pixels.show()
            self._onComplete("delete")
            return

        if event.key_number == 11:
            self._pixels[11] = self._activeGreen
            self._pixels.show()
            self._onComplete(OPTIONS[self._optionIndex])
            return

    def __onKeyUp(self, event: KeyEvent):
        if self._pixels is None:
            return
        self.__updateView()
        self.__initPixels()

    def __onEncChange(self, event: EncoderEvent):
        self._optionIndex = (self._optionIndex + event.delta) % len(OPTIONS)
        self.__updateView()
        self.__initPixels()

    def __onEncSwitchDown(self, event: EncoderEvent):
        self._onComplete(OPTIONS[self._optionIndex])

    def __updateView(self):
        self._view.setTitle(_truncate(self._title))
        self._view.setTertiaryLabel("DEL")
        labelKey = "> label" if self._optionIndex == 0 else "  label"
        labelValue = self._value.getSettingString("label")
        self._view.setText(0, _truncate(f"{labelKey}: {labelValue}"))
        colorKey = "> color" if self._optionIndex == 1 else "  color"
        colorValue = "#" + self._value.getSettingString("color").upper()
        self._view.setText(1, _truncate(f"{colorKey}: {colorValue}"))
        codesKey = "> codes" if self._optionIndex == 2 else "  codes"
        codesValue = self._value.getSettingString("codes")
        self._view.setText(2, _truncate(f"{codesKey}: {codesValue}"))
        self._view.show()

    def __initPixels(self):
        self._pixels.fill(0x000000)
        for i in range(3):
            pixelIndex = i * 3
            color = self._focusOrange if self._optionIndex == i else self._dimOrange
            self._pixels[pixelIndex] = color
        self._pixels[9] = self._dimRed
        self._pixels[10] = self._dimYellow
        self._pixels[11] = self._dimGreen
        self._pixels.show()

    def update(self):
        pass

    def connect(self, macroPad: MacroPad, eventBus: EventBus):
        macroPad.pixels.auto_write = False
        macroPad.pixels.brightness = 0.2
        macroPad.display.root_group = self._view.group
        self._pixels = macroPad.pixels
        self.__updateView()
        self.__initPixels()
        eventBus.setOnKeyDown(self.__onKeyDown)
        eventBus.setOnKeyUp(self.__onKeyUp)
        eventBus.setOnEncChange(self.__onEncChange)
        eventBus.setOnEncSwitchDown(self.__onEncSwitchDown)

    def disconnect(self):
        if self._pixels is not None:
            self._pixels.fill(0x000000)
            self._pixels.show()
            self._pixels = None
