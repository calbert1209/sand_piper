from displayio import Group
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text.label import Label


class Display:
    """ Represents a 3 x 4 matrix of keys on screen """

    _black = 0x000000
    _white = 0xFFFFFF
    _font = terminalio.FONT

    def __createGroup(self, width, height, foreColor, backColor):
        font = terminalio.FONT
        group = Group()
        for i in range(12):
            x = i % 3
            y = i // 3
            keyX = (width - 1) * x / 2
            keyY = height - 1 - (3 - y) * 12
            anchorPoint = (x / 2, 1.0)
            keyLabel = Label(font,
                             text='',
                             color=foreColor,
                             anchored_position=(keyX, keyY),
                             anchor_point=anchorPoint)
            group.append(keyLabel)

        titleBack = Rect(0, 0, width, 12, fill=foreColor)
        group.append(titleBack)
        titleText = Label(font,
                          text='',
                          color=backColor,
                          anchored_position=(width//2, -2),
                          anchor_point=(0.5, 0.0))
        group.append(titleText)
        return group

    def __init__(self, macropad):
        self.macropad = macropad
        width = macropad.display.width
        height = macropad.display.height
        group = self.__createGroup(width,
                                   height,
                                   foreColor=self._white,
                                   backColor=self._black)
        self.group = group
        self.macropad.display.root_group = group

    def setText(self, i, value):
        self.group[i].text = value

    def show(self):
        self.macropad.display.refresh()
