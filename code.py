from adafruit_macropad import MacroPad
from sand_piper.Models.Keycodes import KeyCodes
from sand_piper.Models.Model import KeySettings
from sand_piper.Models.RgbValue import RGBValue
from sand_piper.Pages.EditKeyCodes.Display import EditKeyCodesDisplay
from sand_piper.Pages.EditKeyCodes.ViewModel import EditKeyCodesViewModel
from sand_piper.Pages.EditSettings.ViewModel import EditSettingsViewModel
from sand_piper.Pages.EditSettings.Display import EditSettingsDisplay
from sand_piper.Pages.EditLabel.Display import EditLabelDisplay
from sand_piper.Pages.EditLabel.ViewModel import EditLabelViewModel
from sand_piper.Pages.EditColor.Display import EditColorDisplay
from sand_piper.Pages.EditColor.ViewModel import EditColorViewModel
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
        if len(routes) > 1:
            routes.pop()
        return
    if key == "label":
        routes.append("edit_label")
        return
    if key == "color":
        routes.append("edit_color")
        return
    if key == "keyCodes":
        routes.append("edit_codes")
        return

    print("Something went wrong.")


def onCompleteEditLabel(resp: str | None):
    if resp != None:
        global dummyValue
        dummyValue = dummyValue.clone(label=resp)

    if len(routes) > 1:
        routes.pop()


def onCompleteEditColor(resp: tuple[int, int, int] | None):
    if resp != None:
        (r, g, b) = resp
        global dummyValue
        dummyValue = dummyValue.clone(color=RGBValue(r, g, b))

    if len(routes) > 1:
        routes.pop()


def onCompleteEditCodes(resp: list[str] | None):
    if resp != None:
        codes = [KeyCodes.factory(value) for value in resp]
        global dummyValue
        dummyValue = dummyValue.clone(keyCodes=codes)

    if len(routes) > 1:
        routes.pop()


def getPagePerRoute(route: str):
    if route == "edit_settings":
        display = EditSettingsDisplay(macroPad=macroPad)
        return EditSettingsViewModel(
            view=display,
            initialValue=dummyValue,
            onComplete=onCompleteSettingsMenu)
    if route == "edit_label":
        display = EditLabelDisplay(macroPad=macroPad)
        return EditLabelViewModel(
            view=display,
            initialValue=dummyValue.getSettingString("label"),
            onComplete=onCompleteEditLabel)
    if route == "edit_color":
        display = EditColorDisplay(macroPad=macroPad)
        return EditColorViewModel(
            view=display,
            initialValue=dummyValue.getSetting("color"),
            onComplete=onCompleteEditColor)
    if route == "edit_codes":
        display = EditKeyCodesDisplay(macroPad=macroPad)
        return EditKeyCodesViewModel(
            view=display,
            initialValues=[
                k.valueString for k in dummyValue.getSetting("codes")],
            onComplete=onCompleteEditCodes)

    return None


def navigate(route: str):
    vm = getPagePerRoute(route)
    vm.connect(macroPad=macroPad, eventBus=eventBus)
    return vm


viewModel = None

while True:
    if routes[-1] != currentRoute:
        if viewModel != None:
            viewModel.disconnect()
            eventBus.requestReset()
        currentRoute = routes[-1]
        viewModel = navigate(currentRoute)

    eventBus.update()
    viewModel.update()
