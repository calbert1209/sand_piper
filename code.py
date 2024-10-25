from adafruit_macropad import MacroPad
from sand_piper.Models.Model import KeySettings
from sand_piper.Models.RgbValue import RGBValue
from sand_piper.Pages.EditSettings.ViewModel import EditSettingsViewModel
from sand_piper.Pages.EditSettings.Display import EditSettingsDisplay
from sand_piper.EventBus import EventBus


def onComplete(result):
    print(result)


# class KeySettings:
#     def __init__(self, label: str, color: RGBValue, keyCodes: list[str]) -> None:
#         self._label = label
#         self._color = color
#         self._codes = keyCodes

#     def getSetting(self, key):
#         if key == "label":
#             return self._label
#         if key == "color":
#             return self._color
#         if key == "keyCodes" or key == "codes":
#             return self._codes

#         raise Exception(f"Invalid key: `{key}`")

#     def getSettingString(self, key):
#         if key == "label":
#             return self._label
#         if key == "color":
#             return self._color.hexaDecimalString
#         if key == "keyCodes" or key == "codes":
#             return "".join(self._codes)

#         raise Exception(f"Invalid key: `{key}`")


# dummyValue = {
#     "label": "DUDE",
#     "color": RGBValue(255, 64, 0),
#     "keyCodes": ["+CTRL", "+ALT", "+A"]
# }

dummyValue = KeySettings(label="DUDE", color=RGBValue(
    255, 64, 0), keyCodes=["+CTRL", "+ALT", "+A"])

macroPad = MacroPad()
eventBus = EventBus(macroPad)
display = EditSettingsDisplay(macroPad)
viewModel = EditSettingsViewModel(
    view=display, initialValue=dummyValue, onComplete=onComplete)
viewModel.connect(eventBus=eventBus, macroPad=macroPad)

while True:
    eventBus.update()
    viewModel.update()
