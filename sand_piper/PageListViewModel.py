from sand_piper.EventBus import EventBus, KeyEvent, EncoderEvent, EncoderSwitchEvent
from sand_piper.Model import ControlPage, KeyCommand


class PageListEventModel:
    def __init__(self, eventBus: EventBus) -> None:
        eventBus.addEventListener('key_down', self.__onKeyDown)
        eventBus.addEventListener('enc_change', self.__onEncChange)
        eventBus.addEventListener('enc_down', self.__onEncSwitchDown)
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

    def __onKeyDown(self, event: KeyEvent):
        print(event.toStr())

    def __changePage(self, delta: int):
        nextIndex = (self._pageIndex + delta) % len(self._pages)
        self._pageIndex = nextIndex
        self._keyIndex = 0

    def __changeKey(self, delta: int):
        page = self.currentPage
        nextIndex = (self._keyIndex + delta) % len(page.keys)
        self._keyIndex = nextIndex

    def __onEncChange(self, event: EncoderEvent):
        if self._edit:
            self.__changeKey(event.delta)
        else:
            self.__changePage(event.delta)

    def __onEncSwitchDown(self, event: EncoderSwitchEvent):
        nextEdit = not self._edit
        self._edit = nextEdit

    @property
    def currentPage(self):
        return self._pages[self._pageIndex]
