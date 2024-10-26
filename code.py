from adafruit_macropad import MacroPad
from sand_piper.Models.Model import KeySettings
from sand_piper.Models.RgbValue import RGBValue
from sand_piper.Pages.EditKeyCodes.ViewModel import EditKeyCodesViewModel
from sand_piper.Pages.EditKeyCodes.Display import EditKeyCodesDisplay
from sand_piper.EventBus import EventBus


def onComplete(result):
    print(result)


dummyValue = KeySettings(label="DUDE", color=RGBValue(
    255, 64, 0), keyCodes=["+CTRL", "+ALT", "+A"])

macroPad = MacroPad()
eventBus = EventBus(macroPad)
display = EditKeyCodesDisplay(macroPad)
viewModel = EditKeyCodesViewModel(
    view=display, initialValues=["+CTRL", "+ALT", "+A"], onComplete=onComplete)
viewModel.connect(eventBus=eventBus, macroPad=macroPad)

while True:
    eventBus.update()
    viewModel.update()
