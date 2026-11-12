from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus
from sand_piper.Models.Keycodes import KeyCodes
from sand_piper.Models.Model import ControlPage, KeySettings
from sand_piper.Models.RgbValue import RGBValue
from sand_piper.Pages.EditColor.Display import EditColorDisplay
from sand_piper.Pages.EditColor.ViewModel import EditColorViewModel
from sand_piper.Pages.EditKeyCodes.Display import EditKeyCodesDisplay
from sand_piper.Pages.EditKeyCodes.ViewModel import EditKeyCodesViewModel
from sand_piper.Pages.EditLabel.Display import EditLabelDisplay
from sand_piper.Pages.EditLabel.ViewModel import EditLabelViewModel
from sand_piper.Pages.EditPage.ViewModel import EditPageViewModel
from sand_piper.Pages.EditSettings.Display import EditSettingsDisplay
from sand_piper.Pages.EditSettings.ViewModel import EditSettingsViewModel
from sand_piper.Pages.KeyGrid.Display import KeyGridDisplay
from sand_piper.Pages.KeyGrid.ViewModel import KeyGridViewModel
from sand_piper.Storage import loadPagesFromNvm, savePagesToNvm

macroPad = MacroPad()
macroPad.display.auto_refresh = False
macroPad.pixels.auto_write = False

pages = loadPagesFromNvm()

# Boot into settings mode only when the rotary encoder button is held at startup
settingsMode = bool(macroPad.encoder_switch)
ignoreInitialEncSwitch = settingsMode

eventBus = EventBus(macroPad)

routes = ["key_grid"]
currentRoute = ""
activePageIndex = 0
activeKeyIndex = 0


def getCurrentKeySettings() -> KeySettings:
    return pages[activePageIndex].keys[activeKeyIndex]


def setCurrentKeySettings(updated: KeySettings):
    pages[activePageIndex].keys[activeKeyIndex] = updated


def onSelectKeyToEdit(pageIndex: int, keyIndex: int):
    global activePageIndex, activeKeyIndex
    activePageIndex = pageIndex
    activeKeyIndex = keyIndex
    routes.append("edit_settings")


def onOpenPageMenu(pageIndex: int):
    global activePageIndex
    activePageIndex = pageIndex
    routes.append("edit_page")


def onAddPage():
    global activePageIndex
    newPageNumber = len(pages) + 1
    newPage = ControlPage.empty(f"PAGE {newPageNumber}")
    pages.append(newPage)
    activePageIndex = len(pages) - 1
    routes.append("edit_page_title")


def onSaveAndExitSettings():
    savePagesToNvm(pages)
    try:
        import microcontroller

        microcontroller.reset()
    except Exception as err:
        print("Reset failed:", err)


def onCompletePageMenu(action):
    global activePageIndex
    if action is None:
        if len(routes) > 1:
            routes.pop()
        return

    if action == "title":
        routes.append("edit_page_title")
        return

    if action == "delete":
        if len(pages) > 1:
            pages.pop(activePageIndex)
            if activePageIndex >= len(pages):
                activePageIndex = len(pages) - 1
        if len(routes) > 1:
            routes.pop()
        return


def onCompleteEditPageTitle(resp):
    if resp is not None and len(resp) > 0:
        pages[activePageIndex].name = resp

    if len(routes) > 1:
        routes.pop()


def onCompleteSettingsMenu(key):
    """Part of router"""
    if key is None:
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


def onCompleteEditLabel(resp):
    if resp is not None:
        current = getCurrentKeySettings()
        setCurrentKeySettings(current.clone(label=resp))

    if len(routes) > 1:
        routes.pop()


def onCompleteEditColor(resp):
    if resp is not None:
        (r, g, b) = resp
        current = getCurrentKeySettings()
        setCurrentKeySettings(current.clone(color=RGBValue(r, g, b)))

    if len(routes) > 1:
        routes.pop()


def onCompleteEditCodes(resp):
    if resp is not None:
        codes = [KeyCodes.factory(value) for value in resp]
        current = getCurrentKeySettings()
        setCurrentKeySettings(current.clone(keyCodes=codes))

    if len(routes) > 1:
        routes.pop()


def getPagePerRoute(route: str):
    global ignoreInitialEncSwitch
    if route == "key_grid":
        display = KeyGridDisplay(macroPad=macroPad)
        ignoreSwitch = ignoreInitialEncSwitch
        ignoreInitialEncSwitch = False
        return KeyGridViewModel(
            view=display,
            pages=pages,
            initialPageIndex=activePageIndex,
            settingsMode=settingsMode,
            ignoreInitialEncSwitch=ignoreSwitch,
            onSelectKey=onSelectKeyToEdit,
            onOpenPageMenu=onOpenPageMenu,
            onAddPage=onAddPage,
            onSaveAndExit=onSaveAndExitSettings,
        )
    if route == "edit_page":
        display = EditSettingsDisplay(macroPad=macroPad)
        return EditPageViewModel(
            view=display,
            page=pages[activePageIndex],
            canDelete=len(pages) > 1,
            onComplete=onCompletePageMenu,
        )
    if route == "edit_page_title":
        display = EditLabelDisplay(macroPad=macroPad)
        return EditLabelViewModel(
            view=display,
            initialValue=pages[activePageIndex].name,
            onComplete=onCompleteEditPageTitle,
            maxLength=15,
        )
    if route == "edit_settings":
        display = EditSettingsDisplay(macroPad=macroPad)
        return EditSettingsViewModel(
            view=display,
            initialValue=getCurrentKeySettings(),
            onComplete=onCompleteSettingsMenu,
            title=f"KEY {activeKeyIndex + 1}",
        )
    if route == "edit_label":
        display = EditLabelDisplay(macroPad=macroPad)
        return EditLabelViewModel(
            view=display,
            initialValue=getCurrentKeySettings().getSettingString("label"),
            onComplete=onCompleteEditLabel,
            maxLength=7,
        )
    if route == "edit_color":
        display = EditColorDisplay(macroPad=macroPad)
        return EditColorViewModel(
            view=display,
            initialValue=getCurrentKeySettings().getSetting("color"),
            onComplete=onCompleteEditColor,
        )
    if route == "edit_codes":
        display = EditKeyCodesDisplay(macroPad=macroPad)
        return EditKeyCodesViewModel(
            view=display,
            initialValues=[
                k.valueString for k in getCurrentKeySettings().getSetting("codes")
            ],
            onComplete=onCompleteEditCodes,
        )

    return None


def navigate(route: str):
    vm = getPagePerRoute(route)
    vm.connect(macroPad=macroPad, eventBus=eventBus)
    return vm


viewModel = None

while True:
    if routes[-1] != currentRoute:
        if viewModel is not None:
            viewModel.disconnect()
            eventBus.requestReset()
        currentRoute = routes[-1]
        viewModel = navigate(currentRoute)

    eventBus.update()
    viewModel.update()
