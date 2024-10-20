from adafruit_macropad import MacroPad
from sand_piper.Pages.EditLabel.Display import EditLabelDisplay
from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent
from sand_piper.PaginationManager import PaginationManager

OPTIONS = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z", "."]


class EditLabelViewModel:
    _scrollIndex = 1

    def __init__(self, macroPad: MacroPad, initialValue: str, onComplete):
        self._view = EditLabelDisplay(macroPad)
        self._macroPad = macroPad
        self._pixels = macroPad.pixels
        self._value = list(initialValue)
        self._options = PaginationManager(
            items=OPTIONS, pageSize=9, repeating=True)
        self._onComplete = onComplete

    def __delete(self):
        if len(self._value) > 0:
            self._value.pop()

    def __onKeyDown(self, event: KeyEvent):
        if event.key_number == 10:
            self.__delete()
            return

        if event.key_number < 9:
            options = self._options.currentPage
            # final page of options may have less than 9 options
            if event.key_number < len(options):
                self._value.append(options[event.key_number])
            return

        if event.key_number == 9:
            self._onComplete(None)

        if event.key_number == 11:
            self._onComplete(self._valueString)

    def __onEncChange(self, event: EncoderEvent):
        self._options.move(event.delta)

    @property
    def _valueString(self):
        return "".join(self._value)

    def __updateView(self):
        self._view.setTitle(self._valueString + "_")
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

    def disconnect(self, eventBus: EventBus):
        eventBus.setOnKeyDown(None)
        eventBus.setOnEncChange(None)
