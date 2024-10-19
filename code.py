from adafruit_macropad import MacroPad
from sand_piper.EventBus import EventBus
from sand_piper.EditColorDisplay import EditColorDisplay
from sand_piper.ColorEditViewModel import ColorEditViewModel


macroPad = MacroPad()
eventBus = EventBus(macroPad)
display = EditColorDisplay(macroPad)
viewModel = ColorEditViewModel(
    eventBus=eventBus, view=display, macroPad=macroPad, initialRgb=(255, 0, 0))

viewModel.update()

while True:
    eventBus.update()
    viewModel.update()
