from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus

macroPad = MacroPad()

eventBus = EventBus(macroPad)

while True:
    eventBus.update()

    while len(eventBus.events) > 0:
        event = eventBus.events.pop(0)
        status = eventBus.toString(event)
        print(status)
