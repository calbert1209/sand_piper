
from sand_piper.Models.KeyCodes import KeyCode
from sand_piper.Models.RgbValue import RGBValue


class KeyCommand:
    def __init__(self, label: str) -> None:
        self.label = label


class ControlPage:
    def __init__(self, name: str, keys: list[KeyCommand]) -> None:
        self.name = name
        self.keys = keys


class KeySettings:
    def __init__(self, label: str, color: RGBValue, keyCodes: list[KeyCode]) -> None:
        self._label = label
        self._color = color
        self._codes = keyCodes

    def getSetting(self, key):
        if key == "label":
            return self._label
        if key == "color":
            return self._color
        if key == "keyCodes" or key == "codes":
            return self._codes

        raise Exception(f"Invalid key: `{key}`")

    def getSettingString(self, key: str):
        if key == "label":
            return self._label
        if key == "color":
            return self._color.hexaDecimalString
        if key == "keyCodes" or key == "codes":
            return "".join([code.valueString for code in self._codes])

        raise Exception(f"Invalid key: `{key}`")
