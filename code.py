from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus
from sand_piper.EditColorDisplay import Display
from sand_piper.PageListViewModel import PageListEventModel


macroPad = MacroPad()
macroPad.display.auto_refresh = False
macroPad.pixels.auto_write = False
eventBus = EventBus(macroPad)
viewModel = PageListEventModel(eventBus)
display = Display(macroPad)
# bind display group to macroPad group
macroPad.display.root_group = display.group


def updateView(vm: PageListEventModel, v: Display):
    for i in range(len(vm.currentPage.keys) - 9):
        keyControl = vm.currentPage.keys[i]
        label = keyControl.label
        if vm._edit and vm._keyIndex == i:
            label = "|{}|".format(label)
        v.setText(i, label)

    pageTitle = vm.currentPage.name
    if vm._edit:
        pageTitle = "[{}]".format(vm.currentPage.name)

    v.setTitle(pageTitle)
    v.setPrimaryLabel(f"{vm.currentPage.name}")
    v.setSecondaryLabel("no")
    v.setTertiaryLabel("DEL")
    v.show()


while True:
    eventBus.update()
    updateView(vm=viewModel, v=display)
