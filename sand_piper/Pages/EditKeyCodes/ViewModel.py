from adafruit_macropad import MacroPad
from sand_piper.Models.KeyCodes import KeyCodes
from sand_piper.Pages.EditKeyCodes.Display import EditKeyCodesDisplay
from sand_piper.EventBus import EncoderSwitchEvent, EventBus, KeyEvent, EncoderEvent
from sand_piper.PaginationManager import PaginationManager


class EditKeyCodesViewModel:
    _scrollIndex = 1
    _pressMode = True

    def __init__(self, macroPad: MacroPad, initialValue: str, onComplete):
        self._view = EditKeyCodesDisplay(macroPad)
        self._macroPad = macroPad
        self._pixels = macroPad.pixels
        self._values = [{"sign": "+", "value": c} for c in list(initialValue)]
        self._options = PaginationManager(
            items=KeyCodes.keys, pageSize=9, repeating=True)
        self._onComplete = onComplete

    def __delete(self):
        if len(self._values) > 0:
            self._values.pop()

    def __onKeyDown(self, event: KeyEvent):
        if event.key_number == 10:
            self.__delete()
            return

        if event.key_number < 9:
            options = self._options.currentPage
            # final page of options may have less than 9 options
            if event.key_number < len(options):
                self._values.append({
                    "value": options[event.key_number],
                    "sign": self._sign
                })
            return

        if event.key_number == 9:
            self._onComplete(None)

        if event.key_number == 11:
            values = [f"{k["sign"]}{
                KeyCodes.entries[k["value"]]}" for k in self._values]
            # self._onComplete(self._valueString)
            self._onComplete(values)

    def __onEncChange(self, event: EncoderEvent):
        print(event.delta)
        self._options.move(event.delta)

    def __onEncSwitchDown(self, event: EncoderSwitchEvent):
        self._pressMode = not self._pressMode

    @property
    def _sign(self):
        if self._pressMode:
            return "+"
        return "-"

    @property
    def _valence(self):
        if self._pressMode:
            return 1
        return -1

    @property
    def _valueString(self):
        output = ""
        for item in self._values:
            output += f"{item["sign"]}{item["value"]}"
        return output

    def __updateView(self):
        self._view.setTitle(self._valueString + self._sign)
        options = self._options.currentPage
        for i in range(9):
            # final page of options may have less than 9 options
            if i < len(options):
                self._view.setText(i, options[i])
            else:
                self._view.setText(i, "")

    def __updatePixels(self):
        pass

    def update(self):
        self.__updateView()
        self.__updatePixels()

    def connect(self, macroPad: MacroPad, eventBus: EventBus):
        macroPad.pixels.auto_write = False
        macroPad.pixels.brightness = 0.2
        macroPad.display.root_group = self._view.group
        eventBus.setOnKeyDown(self.__onKeyDown)
        eventBus.setOnEncChange(self.__onEncChange)
        eventBus.setOnEncSwitchDown(self.__onEncSwitchDown)

    def disconnect(self, eventBus: EventBus):
        eventBus.setOnKeyDown(None)
        eventBus.setOnEncChange(None)
        eventBus.setOnEncSwitchDown(None)
