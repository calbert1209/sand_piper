from adafruit_macropad import MacroPad
from sand_piper.EventBus import EncoderEvent, EventBus, KeyEvent
from sand_piper.Models.Model import ControlPage
from sand_piper.Pages.EditSettings.Display import EditSettingsDisplay


def _truncate(text: str, maxLen: int = 21) -> str:
    if len(text) > maxLen:
        return text[:maxLen - 2] + ".."
    return text


class EditPageViewModel:
    _dimOrange = 0x160800
    _focusOrange = 0xAA3300
    _activeOrange = 0xEE4400
    _dimRed = 0x330000
    _activeRed = 0xDD0000
    _dimGreen = 0x003300
    _activeGreen = 0x00DD00

    def __init__(
        self,
        view: EditSettingsDisplay,
        page: ControlPage,
        canDelete: bool,
        onComplete,
    ):
        self._view = view
        self._page = page
        self._canDelete = canDelete
        self._onComplete = onComplete
        self._optionIndex = 0
        self._pixels = None

    def __onKeyDown(self, event: KeyEvent):
        if event.key_number == 0:
            self._optionIndex = 0
            self._pixels[0] = self._activeOrange
            self._pixels.show()
            self._onComplete("title")
            return

        if event.key_number == 3 and self._canDelete:
            self._optionIndex = 1
            self._pixels[3] = self._activeOrange
            self._pixels.show()
            self._onComplete("delete")
            return

        if event.key_number == 9:
            self._pixels[9] = self._activeRed
            self._pixels.show()
            self._onComplete(None)
            return

        if event.key_number == 11:
            self._pixels[11] = self._activeGreen
            self._pixels.show()
            if self._optionIndex == 0:
                self._onComplete("title")
            elif self._optionIndex == 1 and self._canDelete:
                self._onComplete("delete")
            return

    def __onKeyUp(self, event: KeyEvent):
        if self._pixels is None:
            return
        self.__updateView()
        self.__initPixels()

    def __onEncChange(self, event: EncoderEvent):
        if not self._canDelete:
            return
        self._optionIndex = (self._optionIndex + event.delta) % 2
        self.__updateView()
        self.__initPixels()

    def __onEncSwitchDown(self, event: EncoderEvent):
        if self._optionIndex == 0:
            self._onComplete("title")
        elif self._optionIndex == 1 and self._canDelete:
            self._onComplete("delete")

    def __updateView(self):
        self._view.setTitle(_truncate(f"PAGE: {self._page.name}"))
        self._view.setPrimaryLabel(
            "DEL" if (self._optionIndex == 1 and self._canDelete) else "EDIT"
        )
        titlePrefix = "> title" if self._optionIndex == 0 else "  title"
        self._view.setText(0, _truncate(f"{titlePrefix}: {self._page.name}"))
        if self._canDelete:
            delPrefix = "> delete page" if self._optionIndex == 1 else "  delete page"
            self._view.setText(1, delPrefix)
        else:
            self._view.setText(1, "  (only page)")
        self._view.setText(2, "")
        self._view.show()

    def __initPixels(self):
        self._pixels.fill(0x000000)
        self._pixels[0] = (
            self._focusOrange if self._optionIndex == 0 else self._dimOrange
        )
        if self._canDelete:
            self._pixels[3] = (
                self._focusOrange if self._optionIndex == 1 else self._dimOrange
            )
        self._pixels[9] = self._dimRed
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
