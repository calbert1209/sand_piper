from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus, HidEvent

macroPad = MacroPad()


def reportHidEvent(event: HidEvent):
    print(event.toStr())


eventBus = EventBus(macroPad)

for type in ["key_down", "key_up", "enc_down", "enc_up", "enc_change"]:
    eventBus.addEventListener(type, reportHidEvent)


while True:
    eventBus.update()
