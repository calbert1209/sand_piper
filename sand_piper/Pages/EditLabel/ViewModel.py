from adafruit_macropad import MacroPad
from sand_piper.Pages.EditLabel.Display import EditLabelDisplay
from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent
from sand_piper.PaginationManager import PaginationManager

OPTIONS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z", "0",
    "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "SPC", ".", "-", "_", "/", "+", "*",
]


class EditLabelViewModel:
    _dimOrange = 0x160800
    _activeOrange = 0xEE4400
    _dimRed = 0x330000
    _activeRed = 0xDD0000
    _dimYellow = 0x332200
    _activeYellow = 0xDDAA00
    _dimGreen = 0x003300
    _activeGreen = 0x00DD00

    def __init__(
        self,
        view: EditLabelDisplay,
        initialValue: str,
        onComplete,
        maxLength: int = 7,
    ):
        self._view = view
        self._value = list(initialValue[:maxLength])
        self._maxLength = maxLength
        self._options = PaginationManager(
            items=OPTIONS, pageSize=9, repeating=True)
        self._onComplete = onComplete
        self._pixels = None

    def __delete(self):
        if len(self._value) > 0:
            self._value.pop()

    def __onKeyDown(self, event: KeyEvent):
        if event.key_number == 10:
            self.__delete()
            self.__updateView()
            if self._pixels is not None:
                self._pixels[10] = self._activeYellow
                self._pixels.show()
            return

        if event.key_number < 9:
            options = self._options.currentPage
            # final page of options may have less than 9 options
            if event.key_number < len(options) and options[event.key_number] != "":
                if len(self._value) < self._maxLength:
                    selected = options[event.key_number]
                    char = " " if selected == "SPC" else selected
                    self._value.append(char)
                self.__updateView()
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
            self._onComplete(self._valueString)
            return

    def __onKeyUp(self, event: KeyEvent):
        self.__updatePixels()

    def __onEncChange(self, event: EncoderEvent):
        self._options.move(event.delta)
        self.__updateView()
        self.__updatePixels()

    @property
    def _valueString(self):
        return "".join(self._value)

    def __updateView(self):
        remaining = max(0, self._maxLength - len(self._value))
        rawTitle = self._valueString + ("_" * remaining)
        title = rawTitle[-21:] if len(rawTitle) > 21 else rawTitle
        self._view.setTitle(title)
        options = self._options.currentPage
        for i in range(9):
            # final page of options may have less than 9 options
            if i < len(options):
                self._view.setText(i, options[i])
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
        self.__updateView()
        self.__updatePixels()

    def disconnect(self):
        if self._pixels is not None:
            self._pixels.fill(0x000000)
            self._pixels.show()
            self._pixels = None
