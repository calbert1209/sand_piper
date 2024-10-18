from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus
from sand_piper.EditColorDisplay import Display
from sand_piper.ColorEditViewModel import ColorEditViewModel


macroPad = MacroPad()
macroPad.display.auto_refresh = False
macroPad.pixels.auto_write = False
eventBus = EventBus(macroPad)
viewModel = ColorEditViewModel(eventBus, (255, 0, 0))
display = Display(macroPad)
# bind display group to macroPad group
macroPad.display.root_group = display.group
macroPad.pixels.brightness = 0.2


def initView(vm: ColorEditViewModel, v: Display):
    v.setPrimaryLabel("OK")
    v.setSecondaryLabel("X")
    v.show()


def updateView(vm: ColorEditViewModel, v: Display):
    v.setText(0, vm.redValue)
    v.setText(1, vm.greenValue)
    v.setText(2, vm.blueValue)
    pageTitle = vm.valueString()
    v.setTitle(pageTitle)
    v.show()


def updatePixels(vm: ColorEditViewModel):
    for i in [1, 2, 4, 5, 7, 8]:
        macroPad.pixels[i] = vm.hexValue

    macroPad.pixels[0] = 0xff0000
    macroPad.pixels[3] = 0x00ff00
    macroPad.pixels[6] = 0x0000ff
    macroPad.pixels[9] = 0xff0000
    macroPad.pixels[11] = 0x00ff00
    macroPad.pixels.show()


initView(vm=viewModel, v=display)

while True:
    eventBus.update()
    updateView(vm=viewModel, v=display)
    updatePixels(vm=viewModel)
