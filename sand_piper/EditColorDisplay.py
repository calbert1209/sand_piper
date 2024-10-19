# cspell:ignore displayio, terminalio, adafruit
from displayio import Group
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text.label import Label

row3KeyXMap = [8, 65, 117]
keyYMap = [25, 37, 49, 63]
defaultMenuLabels = ["BACK", "", "OK"]

BANNER_HEIGHT = 11
BANNER_WIDTH = 42


class Display:
    """ Represents a 3 x 4 matrix of keys on screen """

    _black = 0x000000
    _white = 0xFFFFFF
    _font = terminalio.FONT

    def __createOptions(self, group):
        width = self.macroPad.display.width
        for i in range(6):
            x = i % 3
            y = i // 3
            keyX = (width - 1) * x / 2
            keyY = keyYMap[y+1]
            anchorPoint = (x / 2, 1.0)
            keyLabel = Label(self._font,
                             text='',
                             color=self._white,
                             anchored_position=(keyX, keyY),
                             anchor_point=anchorPoint)
            # group[i]
            group.append(keyLabel)

    def __createMenu(self, group):
        keyY = keyYMap[3]
        backWidth = BANNER_WIDTH + 1
        for x in range(3):
            keyX = row3KeyXMap[x]
            back = Rect(x * backWidth, keyY-BANNER_HEIGHT,
                        BANNER_WIDTH, BANNER_HEIGHT, fill=self._white)
            anchorPoint = (x / 2, 1.0)
            # 6, 8, 10
            group.append(back)
            keyLabel = Label(self._font,
                             text=defaultMenuLabels[x],
                             color=self._black,
                             anchored_position=(keyX, keyY),
                             anchor_point=anchorPoint)
            # 7, 9, 11
            group.append(keyLabel)

    def __createHeader(self, group):
        width = self.macroPad.display.width
        titleBack = Rect(0, 0, width, BANNER_HEIGHT, fill=self._white)
        # group[12]
        group.append(titleBack)
        titleText = Label(self._font,
                          text='0:0',
                          color=self._black,
                          anchored_position=(width//2, -2),
                          anchor_point=(0.5, 0.0))
        # group[13]
        group.append(titleText)

    def __createGroup(self):
        group = Group()
        # group items 0 ~ 5
        self.__createOptions(group)
        # group items 6 ~ 11
        self.__createMenu(group)
        # group items 12 ~ 13
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
        if i > 5 or i < 0:
            raise Exception(f"Index {i} out of range")

        self.__setText(i, value)

    def setTitle(self, value: str):
        self.__setText(13, value)

    def setSecondaryLabel(self, value: str):
        self.__setText(7, value)

    def setTertiaryLabel(self, value: str):
        self.__setText(9, value)

    def setPrimaryLabel(self, value: str):
        self.__setText(11, value)

    def show(self):
        self.macroPad.display.refresh()
