from adafruit_macropad import MacroPad
from supervisor import ticks_ms
from sand_piper.EventBus import (
    EncoderEvent,
    EncoderSwitchEvent,
    EventBus,
    KeyEvent,
)
from sand_piper.Models.Model import ControlPage
from sand_piper.Pages.KeyGrid.Display import KeyGridDisplay

LONG_PRESS_MS = 1000


class KeyGridViewModel:
    """ViewModel for the 3x4 hotkey grid in both normal hotkey mode and settings selection mode."""

    def __init__(
        self,
        view: KeyGridDisplay,
        pages: list[ControlPage],
        initialPageIndex: int = 0,
        settingsMode: bool = False,
        ignoreInitialEncSwitch: bool = False,
        onSelectKey=None,
        onOpenPageMenu=None,
        onAddPage=None,
        onSaveAndExit=None,
    ) -> None:
        self._view = view
        self._pages = pages
        self._settingsMode = settingsMode
        totalSlots = (len(pages) + 1) if settingsMode else len(pages)
        self._pageIndex = initialPageIndex % max(1, totalSlots)
        self._onSelectKey = onSelectKey
        self._onOpenPageMenu = onOpenPageMenu
        self._onAddPage = onAddPage
        self._onSaveAndExit = onSaveAndExit
        self._macroPad = None
        self._pixels = None
        self._encPressStartMs = None
        self._ignoreRelease = ignoreInitialEncSwitch
        self._readyToSaveAndExit = False

    @property
    def isAddPageScreen(self) -> bool:
        return self._settingsMode and self._pageIndex == len(self._pages)

    @property
    def currentPage(self) -> ControlPage:
        return self._pages[self._pageIndex]

    @property
    def pageIndex(self) -> int:
        return self._pageIndex

    def __refreshPage(self):
        if self.isAddPageScreen:
            self._view.setTitle("+ ADD PAGE +")
            for i in range(12):
                self._view.setText(i, "")
                self._pixels[i] = 0x000000
            self._view.setText(1, "PRESS")
            self._view.setText(4, "[ + NEW ]")
            self._view.setText(7, "TO ADD")
            self._pixels[4] = 0x00DD00
            self._pixels.show()
            self._view.show()
            return

        page = self.currentPage
        title = f"*{page.name}*" if self._settingsMode else page.name
        self._view.setTitle(title)
        for i in range(12):
            if i < len(page.keys):
                keySetting = page.keys[i]
                self._view.setText(i, keySetting.label)
                self._pixels[i] = keySetting.color.hexValue
            else:
                self._view.setText(i, "")
                self._pixels[i] = 0x000000

        if not self._settingsMode and self._macroPad is not None:
            self._macroPad.keyboard.release_all()
            self._macroPad.consumer_control.release()
            self._macroPad.mouse.release_all()
            self._macroPad.stop_tone()

        self._pixels.show()
        self._view.show()

    def __onKeyDown(self, event: KeyEvent):
        key_number = event.key_number

        if self.isAddPageScreen:
            self._pixels[key_number] = 0xFFFFFF
            self._pixels.show()
            if self._onAddPage is not None:
                self._onAddPage()
            return

        page = self.currentPage
        if key_number >= len(page.keys):
            return

        if self._settingsMode:
            self._pixels[key_number] = 0xFFFFFF
            self._pixels.show()
            if self._onSelectKey is not None:
                self._onSelectKey(self._pageIndex, key_number)
            return

        # Normal hotkey mode: light key white and execute press/release sequence
        self._pixels[key_number] = 0xFFFFFF
        self._pixels.show()
        for code in page.keys[key_number].keyCodes:
            if code.press:
                self._macroPad.keyboard.press(code.value)
            else:
                self._macroPad.keyboard.release(code.value)

    def __onKeyUp(self, event: KeyEvent):
        if self.isAddPageScreen:
            return

        key_number = event.key_number
        page = self.currentPage
        if key_number >= len(page.keys):
            return

        if self._settingsMode:
            self._pixels[key_number] = page.keys[key_number].color.hexValue
            self._pixels.show()
            return

        # Release any pressed keys from this macro's sequence and restore LED color
        for code in page.keys[key_number].keyCodes:
            if code.press:
                self._macroPad.keyboard.release(code.value)
        self._pixels[key_number] = page.keys[key_number].color.hexValue
        self._pixels.show()

    def __onEncChange(self, event: EncoderEvent):
        totalSlots = (len(self._pages) + 1) if self._settingsMode else len(self._pages)
        if totalSlots <= 1:
            return
        self._pageIndex = (self._pageIndex + event.delta) % totalSlots
        self.__refreshPage()

    def __onEncSwitchDown(self, event: EncoderSwitchEvent):
        if not self._settingsMode:
            return
        self._ignoreRelease = False
        self._readyToSaveAndExit = False
        self._encPressStartMs = ticks_ms()

    def __onEncSwitchUp(self, event: EncoderSwitchEvent):
        if not self._settingsMode:
            return
        if self._ignoreRelease:
            self._ignoreRelease = False
            self._encPressStartMs = None
            return
        if self._readyToSaveAndExit:
            self._readyToSaveAndExit = False
            self._encPressStartMs = None
            if self._onSaveAndExit is not None:
                self._onSaveAndExit()
            return
        if self._encPressStartMs is not None:
            elapsed = ticks_ms() - self._encPressStartMs
            self._encPressStartMs = None
            if elapsed < LONG_PRESS_MS:
                if self.isAddPageScreen:
                    if self._onAddPage is not None:
                        self._onAddPage()
                else:
                    if self._onOpenPageMenu is not None:
                        self._onOpenPageMenu(self._pageIndex)

    def update(self):
        if (
            self._settingsMode
            and self._encPressStartMs is not None
            and not self._readyToSaveAndExit
        ):
            elapsed = ticks_ms() - self._encPressStartMs
            if elapsed >= LONG_PRESS_MS:
                self._readyToSaveAndExit = True
                self._view.setTitle("SAVING... RELEASE")
                self._view.show()
                if self._pixels is not None:
                    self._pixels.fill(0x00DD00)
                    self._pixels.show()

    def connect(self, macroPad: MacroPad, eventBus: EventBus):
        self._macroPad = macroPad
        self._pixels = macroPad.pixels
        self._encPressStartMs = None
        macroPad.display.auto_refresh = False
        macroPad.pixels.auto_write = False
        macroPad.pixels.brightness = 0.2
        macroPad.display.root_group = self._view.group
        self.__refreshPage()
        eventBus.setOnKeyDown(self.__onKeyDown)
        eventBus.setOnKeyUp(self.__onKeyUp)
        eventBus.setOnEncChange(self.__onEncChange)
        eventBus.setOnEncSwitchDown(self.__onEncSwitchDown)
        eventBus.setOnEncSwitchUp(self.__onEncSwitchUp)

    def disconnect(self):
        self._encPressStartMs = None
        if self._macroPad is not None:
            self._macroPad.keyboard.release_all()
        if self._pixels is not None:
            self._pixels.fill(0x000000)
            self._pixels.show()
            self._pixels = None
        self._macroPad = None
