from adafruit_macropad import MacroPad
from sand_piper.Models.RgbValue import RGBValue
from sand_piper.Pages.EditColor.ViewModel import EditColorViewModel
from sand_piper.Pages.EditColor.Display import EditColorDisplay
from sand_piper.EventBus import EventBus


def onComplete(result):
    print(result)


macroPad = MacroPad()
eventBus = EventBus(macroPad)
display = EditColorDisplay(macroPad)
viewModel = EditColorViewModel(
    view=display, initialRgb=RGBValue(255, 64, 0), onComplete=onComplete)
viewModel.connect(eventBus=eventBus, macroPad=macroPad)

while True:
    eventBus.update()
    viewModel.update()
