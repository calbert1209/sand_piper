from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus, HidEvent

macroPad = MacroPad()


def reportHidEvent(event: HidEvent):
    print(event.toStr())


eventBus = EventBus(macroPad,
                    onKeyDown=reportHidEvent,
                    onKeyUp=reportHidEvent,
                    onEncSwitchDown=reportHidEvent,
                    onEncSwitchUp=reportHidEvent,
                    onEncChange=reportHidEvent)

while True:
    eventBus.update()
