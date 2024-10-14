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
                KeyCommand("VOL+"),
                KeyCommand("VOL-"),
                KeyCommand("MUTE")
            ]),
            ControlPage("Bar", [
                KeyCommand("PREV"),
                KeyCommand("PLAY"),
                KeyCommand("NEXT")
            ])
        ]
        self._pageIndex = 0
        self._edit = False

    def _onKeyDown(self, event: KeyEvent):
        print(event.toStr())

    def _onEncChange(self, event: EncoderEvent):
        nextIndex = (self._pageIndex + event.delta) % len(self._pages)
        self._pageIndex = nextIndex
        print(self.currentPage.name)

    def _onEncSwitchDown(self, event: EncoderSwitchEvent):
        nextEdit = not self._edit
        self._edit = nextEdit

    @property
    def currentPage(self):
        return self._pages[self._pageIndex]
