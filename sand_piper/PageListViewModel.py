from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent, EncoderSwitchEvent
from sand_piper.Model import ControlPage, KeyCommand


class PageListEventModel:
    def __init__(self, eventBus: EventBus) -> None:
        eventBus.addEventListener('key_down', self._onKeyDown)
        eventBus.addEventListener('enc_change', self._onEncChange)
        eventBus.addEventListener('enc_down', self._onEncSwitchDown)
        self._eventBus = eventBus
        self._pages = [
            ControlPage("Foo", [
                KeyCommand("ONE"),
                KeyCommand("TWO"),
                KeyCommand("TRES"),
                KeyCommand("FOUR"),
                KeyCommand("FIVE"),
                KeyCommand("SIX"),
                KeyCommand("SVN"),
                KeyCommand("EIT"),
                KeyCommand("NINE"),
                KeyCommand("BACK"),
                KeyCommand("DEL"),
                KeyCommand("OK"),

            ]),
            ControlPage("Bar", [
                KeyCommand("PREV"),
                KeyCommand("PLAY"),
                KeyCommand("NEXT")
            ])
        ]
        self._pageIndex = 0
        self._keyIndex = 0
        self._edit = False

    def _onKeyDown(self, event: KeyEvent):
        print(event.toStr())

    def _changePage(self, delta: int):
        nextIndex = (self._pageIndex + delta) % len(self._pages)
        self._pageIndex = nextIndex
        self._keyIndex = 0

    def _changeKey(self, delta: int):
        page = self.currentPage
        nextIndex = (self._keyIndex + delta) % len(page.keys)
        self._keyIndex = nextIndex

    def _onEncChange(self, event: EncoderEvent):
        if self._edit:
            self._changeKey(event.delta)
        else:
            self._changePage(event.delta)

    def _onEncSwitchDown(self, event: EncoderSwitchEvent):
        nextEdit = not self._edit
        self._edit = nextEdit

    @property
    def currentPage(self):
        return self._pages[self._pageIndex]
