# cspell:ignore displayio, terminalio, adafruit
from displayio import Group
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text.label import Label

row3KeyXMap = [8, 65, 117]
keyYMap = [25, 37, 49, 63]
defaultMenuLabels = ["BACK", "", "EDIT"]

BANNER_HEIGHT = 11
BANNER_WIDTH = 42


class EditSettingsDisplay:
    """ Represents a 3 x 4 matrix of keys on screen """

    _black = 0x000000
    _white = 0xFFFFFF
    _font = terminalio.FONT

    def __createOptions(self, group):
        for x in range(3):
            keyX = 0
            keyY = keyYMap[x]
            anchorPoint = (0, 1.0)
            keyLabel = Label(self._font,
                             text='',
                             color=self._white,
                             anchored_position=(keyX, keyY),
                             anchor_point=anchorPoint)
            group.append(keyLabel)

    def __createMenu(self, group):
        keyY = keyYMap[3]
        backWidth = BANNER_WIDTH + 1
        for x in range(3):
            keyX = row3KeyXMap[x]
            fill = self._white if defaultMenuLabels[x] != "" else self._black
            back = Rect(x * backWidth, keyY-BANNER_HEIGHT,
                        BANNER_WIDTH, BANNER_HEIGHT, fill=fill)
            anchorPoint = (x / 2, 1.0)
            group.append(back)
            keyLabel = Label(self._font,
                             text=defaultMenuLabels[x],
                             color=self._black,
                             anchored_position=(keyX, keyY),
                             anchor_point=anchorPoint)
            group.append(keyLabel)

    def __createHeader(self, group):
        width = self.macroPad.display.width
        titleBack = Rect(0, 0, width, BANNER_HEIGHT, fill=self._white)
        group.append(titleBack)
        titleText = Label(self._font,
                          text='0:0',
                          color=self._black,
                          anchored_position=(width//2, -2),
                          anchor_point=(0.5, 0.0))
        group.append(titleText)

    def __createGroup(self):
        group = Group()
        # group items 0 ~ 2
        self.__createOptions(group)
        # group items 3 ~ 8
        self.__createMenu(group)
        # group items 9 ~ 10
        self.__createHeader(group)
        return group

    def __init__(self, macroPad):
        self.macroPad = macroPad
        group = self.__createGroup()
        self.group = group
        # self.macroPad.display.root_group = group

    def __setText(self, i: int, value: str):
        self.group[i].text = value

    def setText(self, i: int, value: str):
        if i > 2 or i < 0:
            raise Exception(f"Index {i} out of range")

        self.__setText(i, value)

    def setTitle(self, value: str):
        self.__setText(10, value)

    def setSecondaryLabel(self, value: str):
        self.group[3].fill = self._white if value != "" else self._black
        self.__setText(4, value)

    def setTertiaryLabel(self, value: str):
        self.group[5].fill = self._white if value != "" else self._black
        self.__setText(6, value)

    def setPrimaryLabel(self, value: str):
        self.group[7].fill = self._white if value != "" else self._black
        self.__setText(8, value)

    def show(self):
        self.macroPad.display.refresh()
