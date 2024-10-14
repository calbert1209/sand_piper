from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus
from sand_piper.Display import Display
from sand_piper.PageListViewModel import PageListEventModel


macroPad = MacroPad()
macroPad.display.auto_refresh = False
macroPad.pixels.auto_write = False
eventBus = EventBus(macroPad)
viewModel = PageListEventModel(eventBus)
display = Display(macroPad)


def updateView(vm: PageListEventModel, v: Display):
    for i in range(len(vm.currentPage.keys)):
        keyControl = vm.currentPage.keys[i]
        label = keyControl.label
        if vm._edit and vm._keyIndex == i:
            label = "|{}|".format(label)
        v.setText(i, label)

    pageTitle = vm.currentPage.name
    if vm._edit:
        pageTitle = "[{}]".format(vm.currentPage.name)

    v.setText(13, pageTitle)
    v.show()


while True:
    eventBus.update()
    updateView(vm=viewModel, v=display)
