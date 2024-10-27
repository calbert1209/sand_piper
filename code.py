from adafruit_macropad import MacroPad
from sand_piper.Models.KeyCodes import KeyCodes
from sand_piper.Models.Model import KeySettings
from sand_piper.Models.RgbValue import RGBValue
from sand_piper.Pages.EditColor import ViewModel
from sand_piper.Pages.EditLabel.Display import EditLabelDisplay
from sand_piper.Pages.EditLabel.ViewModel import EditLabelViewModel
from sand_piper.Pages.EditSettings.ViewModel import EditSettingsViewModel
from sand_piper.Pages.EditSettings.Display import EditSettingsDisplay
from sand_piper.EventBus import EventBus

dummyKeyCodes = ["+CTRL", "+ALT", "+A"]

dummyValue = KeySettings(label="DUDE", color=RGBValue(
    255, 64, 0), keyCodes=[KeyCodes.factory(value) for value in dummyKeyCodes])
routes = ["edit_settings"]
currentRoute = ""
macroPad = MacroPad()
eventBus = EventBus(macroPad)


def onComplete(result):
    print(result)


def onCompleteSettingsMenu(key: str | None):
    """ part of router """
    if key == None:
        # print("would pop EditSettings page off of stack")
        if len(routes) > 1:
            routes.pop()
        return
    if key == "label":
        # print("would push EditLabel page onto stack")
        routes.append("edit_label")
        return
    if key == "color":
        print("would push EditColor page onto stack")
        return
    if key == "keyCodes":
        print("would push EditKeyCodes page onto stack")
        return

    print("Something went wrong.")


def getPagePerRoute(route: str):
    if route == "edit_settings":
        display = EditSettingsDisplay(macroPad=macroPad)
        return EditSettingsViewModel(
            view=display, initialValue=dummyValue, onComplete=onCompleteSettingsMenu)
    if route == "edit_label":
        display = EditLabelDisplay(macroPad=macroPad)
        return EditLabelViewModel(view=display, initialValue=dummyValue.getSettingString(
            "label"), onComplete=onCompleteSettingsMenu)

    return None


def renderPage(routes: list[str]):
    if routes[-1] != currentRoute:
        currentRoute = routes[-1]
        vm = getPagePerRoute(currentRoute)
        vm.connect(macroPad=macroPad, eventBus=eventBus)
        return vm

    return None


# viewModel = getPagePerRoute(routes[-1])
# display = EditSettingsDisplay(macroPad)
# viewModel = EditSettingsViewModel(
#     view=display, initialValue=dummyValue, onComplete=onCompleteSettingsMenu)
# viewModel.connect(eventBus=eventBus, macroPad=macroPad)
viewModel = None

while True:
    if routes[-1] != currentRoute:
        if viewModel != None:
            viewModel.disconnect(eventBus)
            eventBus.requestReset()
        currentRoute = routes[-1]
        vm = getPagePerRoute(currentRoute)
        viewModel = vm
        viewModel.connect(macroPad=macroPad, eventBus=eventBus)

    eventBus.update()
    viewModel.update()
