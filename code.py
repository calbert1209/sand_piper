from adafruit_macropad import MacroPad
from sand_piper.EditLabelViewModel import EditLabelViewModel
from sand_piper.EventBus import EventBus
from sand_piper.EditLabelDisplay import EditLabelDisplay


def onComplete(result):
    print(result)


macroPad = MacroPad()
eventBus = EventBus(macroPad)
display = EditLabelDisplay(macroPad)
viewModel = EditLabelViewModel(
    eventBus=eventBus, view=display, macroPad=macroPad, initialValue="DUDE", onComplete=onComplete)

while True:
    eventBus.update()
    viewModel.update()
