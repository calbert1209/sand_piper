# cspell:ignore displayio, terminalio, adafruit
from displayio import Group
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text.label import Label

BANNER_HEIGHT = 13


class KeyGridDisplay:
    """Represents a 3 x 4 matrix of keys on screen with a title header"""

    _black = 0x000000
    _white = 0xFFFFFF
    _font = terminalio.FONT

    def __createGroup(self):
        width = self.macroPad.display.width
        height = self.macroPad.display.height
        group = Group()
        # group items 0 ~ 11: 12 key labels in a 3x4 grid
        for i in range(12):
            x = i % 3
            y = i // 3
            keyX = (width - 1) * x / 2
            keyY = height - 1 - (3 - y) * 12
            anchorPoint = (x / 2, 1.0)
            keyLabel = Label(
                self._font,
                text="",
                color=self._white,
                anchored_position=(keyX, keyY),
                anchor_point=anchorPoint,
            )
            group.append(keyLabel)

        # group[12]: header background rect
        titleBack = Rect(0, 0, width, BANNER_HEIGHT, fill=self._white)
        group.append(titleBack)

        # group[13]: header title text
        titleText = Label(
            self._font,
            text="",
            color=self._black,
            anchored_position=(width // 2, 0),
            anchor_point=(0.5, 0.0),
        )
        group.append(titleText)
        return group

    def __init__(self, macroPad):
        self.macroPad = macroPad
        self.group = self.__createGroup()

    def setText(self, i: int, value: str):
        if i < 0 or i > 11:
            raise Exception(f"Index {i} out of range")
        self.group[i].text = value

    def setTitle(self, value: str):
        self.group[13].text = value
        self.group[12].fill = self._white if value else self._black

    def show(self):
        self.macroPad.display.refresh()

