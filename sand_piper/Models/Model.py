
class KeyCommand:
    def __init__(self, label: str) -> None:
        self.label = label


class ControlPage:
    def __init__(self, name: str, keys: list[KeyCommand]) -> None:
        self.name = name
        self.keys = keys
