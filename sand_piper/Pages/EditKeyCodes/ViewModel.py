from adafruit_macropad import MacroPad
from sand_piper.Models.Keycodes import KeyCodes
from sand_piper.Pages.EditKeyCodes.Display import EditKeyCodesDisplay
from sand_piper.EventBus import EncoderSwitchEvent, EventBus, KeyEvent, EncoderEvent
from sand_piper.PaginationManager import PaginationManager


class EditKeyCodesViewModel:
    _dimOrange = 0x160800
    _activeOrange = 0xEE4400
    _dimRed = 0x330000
    _activeRed = 0xDD0000
    _dimYellow = 0x332200
    _activeYellow = 0xDDAA00
    _dimGreen = 0x003300
    _activeGreen = 0x00DD00

    def __init__(self, view: EditKeyCodesDisplay, initialValues: list[str], onComplete):
        self._view = view
        self._values = [KeyCodes.factory(valueString)
                        for valueString in initialValues]
        self._options = PaginationManager(
            items=KeyCodes.keys, pageSize=9, repeating=True)
        self._onComplete = onComplete
        self._pressMode = True
        self._pixels = None

    def __delete(self):
        if len(self._values) > 0:
            self._values.pop()

    def __onKeyDown(self, event: KeyEvent):
        if event.key_number == 10:
            self.__delete()
            self.__updateView()
            self.__updatePixels()
            if self._pixels is not None:
                self._pixels[10] = self._activeYellow
                self._pixels.show()
            return

        if event.key_number < 9:
            options = self._options.currentPage
            # final page of options may have less than 9 options
            if event.key_number < len(options) and options[event.key_number] != "":
                valueString = f"{self._sign}{options[event.key_number]}"
                self._values.append(KeyCodes.factory(valueString))
                self.__updateView()
                self.__updatePixels()
                if self._pixels is not None:
                    self._pixels[event.key_number] = self._activeOrange
                    self._pixels.show()
            return

        if event.key_number == 9:
            if self._pixels is not None:
                self._pixels[9] = self._activeRed
                self._pixels.show()
            self._onComplete(None)
            return

        if event.key_number == 11:
            if self._pixels is not None:
                self._pixels[11] = self._activeGreen
                self._pixels.show()
            values = [k.valueString for k in self._values]
            self._onComplete(values)

    def __onKeyUp(self, event: KeyEvent):
        if self._pixels is None:
            return
        self.__updateView()
        self.__updatePixels()

    def __onEncChange(self, event: EncoderEvent):
        self._options.move(event.delta)
        self.__updateView()
        self.__updatePixels()

    def __onEncSwitchDown(self, event: EncoderSwitchEvent):
        self._pressMode = not self._pressMode
        self.__updateView()
        self.__updatePixels()

    @property
    def _sign(self):
        if self._pressMode:
            return "+"
        return "-"

    @property
    def _valueString(self):
        output = ""
        for item in self._values:
            output += item.valueString
        return output

    def __updateView(self):
        rawTitle = self._valueString + self._sign
        if len(rawTitle) > 21:
            title = ".." + rawTitle[-19:]
        else:
            title = rawTitle
        self._view.setTitle(title)
        options = self._options.currentPage
        for i in range(9):
            # final page of options may have less than 9 options
            if i < len(options) and options[i] != "":
                self._view.setText(i, f"{self._sign}{options[i]}")
            else:
                self._view.setText(i, "")
        self._view.show()

    def __updatePixels(self):
        if self._pixels is None:
            return
        options = self._options.currentPage
        for i in range(9):
            if i < len(options) and options[i] != "":
                self._pixels[i] = self._dimOrange
            else:
                self._pixels[i] = 0x000000
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
        eventBus.setOnKeyDown(self.__onKeyDown)
        eventBus.setOnKeyUp(self.__onKeyUp)
        eventBus.setOnEncChange(self.__onEncChange)
        eventBus.setOnEncSwitchDown(self.__onEncSwitchDown)
        self.__updateView()
        self.__updatePixels()

    def disconnect(self):
        self._pixels.fill(0x000000)
        self._pixels.show()
        self._pixels = None
