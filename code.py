from adafruit_macropad import MacroPad
from sand_piper.Pages.EditLabel.ViewModel import EditLabelViewModel
from sand_piper.EventBus import EventBus
from sand_piper.Pages.EditLabel.Display import EditLabelDisplay


def onComplete(result):
    print(result)


macroPad = MacroPad()
eventBus = EventBus(macroPad)
viewModel = EditLabelViewModel(
    macroPad=macroPad, initialValue="DUDE", onComplete=onComplete)
viewModel.connect(eventBus=eventBus, macroPad=macroPad)

while True:
    eventBus.update()
    viewModel.update()
