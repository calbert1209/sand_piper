from adafruit_macropad import MacroPad
from sand_piper.Pages.EditKeyCodes.ViewModel import EditKeyCodesViewModel
from sand_piper.EventBus import EventBus


def onComplete(result):
    print(result)


macroPad = MacroPad()
eventBus = EventBus(macroPad)
viewModel = EditKeyCodesViewModel(
    macroPad=macroPad, initialValue="AB", onComplete=onComplete)
viewModel.connect(eventBus=eventBus, macroPad=macroPad)

while True:
    eventBus.update()
    viewModel.update()
