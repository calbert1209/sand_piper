from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus
from sand_piper.EditColorDisplay import Display
from sand_piper.ColorEditViewModel import ColorEditViewModel


macroPad = MacroPad()
macroPad.display.auto_refresh = False
macroPad.pixels.auto_write = False
eventBus = EventBus(macroPad)
display = Display(macroPad)
viewModel = ColorEditViewModel(eventBus, display, macroPad.pixels, (255, 0, 0))
# bind display group to macroPad group
macroPad.display.root_group = display.group
macroPad.pixels.brightness = 0.2

viewModel.update()

while True:
    eventBus.update()
    viewModel.update()
