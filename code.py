from adafruit_macropad import MacroPad
from sand_piper.Models.KeyCodes import KeyCodes
from sand_piper.Models.Model import KeySettings
from sand_piper.Models.RgbValue import RGBValue
from sand_piper.Pages.EditSettings.ViewModel import EditSettingsViewModel
from sand_piper.Pages.EditSettings.Display import EditSettingsDisplay
from sand_piper.EventBus import EventBus

dummyKeyCodes = ["+CTRL", "+ALT", "+A"]

dummyValue = KeySettings(label="DUDE", color=RGBValue(
    255, 64, 0), keyCodes=[KeyCodes.factory(value) for value in dummyKeyCodes])


def onComplete(result):
    print(result)


def onCompleteSettingsMenu(key: str | None):
    """ part of router """
    if key == None:
        print("would pop EditSettings page off of stack")
        return
    if key == "label":
        print("would push EditLabel page onto stack")
        return
    if key == "color":
        print("would push EditColor page onto stack")
        return
    if key == "keyCodes":
        print("would push EditKeyCodes page onto stack")
        return

    print("Something went wrong.")


macroPad = MacroPad()
eventBus = EventBus(macroPad)
display = EditSettingsDisplay(macroPad)
viewModel = EditSettingsViewModel(
    view=display, initialValue=dummyValue, onComplete=onCompleteSettingsMenu)
viewModel.connect(eventBus=eventBus, macroPad=macroPad)

while True:
    eventBus.update()
    viewModel.update()
