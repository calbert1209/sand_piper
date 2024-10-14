from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus, HidEvent, KeyEvent, EncoderEvent

macroPad = MacroPad()


def reportHidEvent(event: HidEvent):
    print(event.toStr())


class KeyCommand:
    def __init__(self, label: str) -> None:
        self.label = label


class ControlPage:
    def __init__(self, name: str) -> None:
        self.name = name
        self.keys = [
            KeyCommand("VOL+"),
            KeyCommand("VOL-"),
            KeyCommand("MUTE")
        ]


class ViewModel:
    def __init__(self, eventBus: EventBus) -> None:
        eventBus.addEventListener('key_down', self._onKeyDown)
        eventBus.addEventListener('enc_change', self._onEncChange)
        self._eventBus = eventBus
        self._pages = [ControlPage("Foo"), ControlPage("Bar")]
        self._pageIndex = 0

    def _onKeyDown(self, event: KeyEvent):
        print(event.toStr())

    def _onEncChange(self, event: EncoderEvent):
        nextIndex = (self._pageIndex + event.delta) % len(self._pages)
        self._pageIndex = nextIndex
        print(self.currentPage.name)

    @property
    def currentPage(self):
        return self._pages[self._pageIndex]


eventBus = EventBus(macroPad)
viewModel = ViewModel(eventBus)


while True:
    eventBus.update()
