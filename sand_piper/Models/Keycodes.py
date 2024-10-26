from adafruit_hid.keycode import Keycode as AdaKeyCode


class KeyCode:
    def __init__(self, value: int, press: bool, label: str) -> None:
        self._value = value
        self._press = press
        self._label = label

    @property
    def value(self):
        return self._value

    @property
    def press(self):
        return self._press

    @property
    def label(self):
        return self._label

    @property
    def valueString(self):
        sign = "+" if self._press else "-"
        return f"{sign}{self._label}"

# cspell:disable


class KeyCodes:
    CTRL = "CTRL"
    SHFT = "SHFT"
    ALT = "ALT"
    OPTION = "OPTION"
    WIN = "WIN"
    CMD = "CMD"
    ESC = "ESC"
    BKSPC = "BKSPC"
    TAB = "TAB"

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"

    ZERO = "ZERO"
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    FOUR = "FOUR"
    FIVE = "FIVE"
    SIX = "SIX"
    SEVEN = "SEVEN"
    EIGHT = "EIGHT"
    NINE = "NINE"
    ENTER = "ENTER"

    SPACE = "SPACE"
    MINUS = "MINUS"
    EQ = "EQ"
    L_BRKT = "L_BRKT"
    R_BRKT = "R_BRKT"
    BKSLSH = "BKSLSH"
    FWDSLSH = "FWDSLSH"
    SEMCLN = "SEMCLN"
    QUOTE = "QUOTE"
    GRAVE = "GRAVE"
    POUND = "POUND"

    MACPWR = "MACPWR"
    UP = "UP"
    COMMA = "COMMA"
    LEFT = "LEFT"
    DOWN = "DOWN"
    RIGHT = "RIGHT"

    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    F9 = "F9"

    keys = [
        "CTRL",
        "SHFT",
        "ALT",
        "OPTION",
        "WIN",
        "CMD",
        "ESC",
        "BKSPC",
        "TAB",

        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",

        "ZERO",

        "ONE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE",
        "ENTER",
        # "RETURN",
        # "ESCAPE",
        # "BACKSPACE",
        # "SPACEBAR",
        "SPACE",
        "MINUS",
        # "EQUALS",
        "EQ",
        # "LEFT_BRACKET",
        "L_BRKT",
        # "RIGHT_BRACKET",
        "R_BRKT",
        # "BACKSLASH",
        "BKSLSH",
        "FWDSLSH",
        # "SEMICOLON",
        "SEMCLN",
        "QUOTE",
        # "GRAVE_ACCENT",
        "GRAVE",
        "POUND",
        # "PERIOD",
        # "FORWARD_SLASH",



        # "CAPS_LOCK",
        # "PRINT_SCREEN",
        # "SCROLL_LOCK",
        # "PAUSE",
        # "INSERT",
        # "HOME",
        # "PAGE_UP",
        # "DELETE",
        # "END",
        # "PAGE_DOWN",

        "MACPWR",
        "UP",
        "COMMA",
        # "LEFT_ARROW",
        "LEFT",
        "DOWN",
        "RIGHT",
        # "DOWN_ARROW",
        # "UP_ARROW",

        # "KEYPAD_NUMLOCK",
        # "KEYPAD_FORWARD_SLASH",
        # "KEYPAD_ASTERISK",
        # "KEYPAD_MINUS",
        # "KEYPAD_PLUS",
        # "KEYPAD_ENTER",
        # "KEYPAD_ONE",
        # "KEYPAD_TWO",
        # "KEYPAD_THREE",
        # "KEYPAD_FOUR",
        # "KEYPAD_FIVE",
        # "KEYPAD_SIX",
        # "KEYPAD_SEVEN",
        # "KEYPAD_EIGHT",
        # "KEYPAD_NINE",
        # "KEYPAD_ZERO",
        # "KEYPAD_PERIOD",
        # "KEYPAD_BACKSLASH",
        # "KEYPAD_EQUALS",

        # "APPLICATION",
        # "W_MENU",
        # "POWER",

        "F1",
        "F2",
        "F3",
        "F4",
        "F5",
        "F6",
        "F7",
        "F8",
        "F9",
        # "F10",
        # "F11",
        # "F12",
        # "F13",
        # "F14",
        # "F15",
        # "F16",
        # "F17",
        # "F18",
        # "F19",
        # "F20",
        # "F21",
        # "F22",
        # "F23",
        # "F24",

        # "LEFT_CONTROL",
        # "CONTROL",
        # "LEFT_SHIFT",
        # "LEFT_ALT",
        # "LEFT_GUI",
        # "GUI",
        # "WINDOWS",
        # "COMMAND",
        # "RIGHT_CONTROL",
        # "RIGHT_SHIFT",
        # "RIGHT_ALT",
        # "RIGHT_GUI",
    ]

    entries = {
        "A": AdaKeyCode.A,
        "B": AdaKeyCode.B,
        "C": AdaKeyCode.C,
        "D": AdaKeyCode.D,
        "E": AdaKeyCode.E,
        "F": AdaKeyCode.F,
        "G": AdaKeyCode.G,
        "H": AdaKeyCode.H,
        "I": AdaKeyCode.I,
        "J": AdaKeyCode.J,
        "K": AdaKeyCode.K,
        "L": AdaKeyCode.L,
        "M": AdaKeyCode.M,
        "N": AdaKeyCode.N,
        "O": AdaKeyCode.O,
        "P": AdaKeyCode.P,
        "Q": AdaKeyCode.Q,
        "R": AdaKeyCode.R,
        "S": AdaKeyCode.S,
        "T": AdaKeyCode.T,
        "U": AdaKeyCode.U,
        "V": AdaKeyCode.V,
        "W": AdaKeyCode.W,
        "X": AdaKeyCode.X,
        "Y": AdaKeyCode.Y,
        "Z": AdaKeyCode.Z,

        "ONE": AdaKeyCode.ONE,
        "TWO": AdaKeyCode.TWO,
        "THREE": AdaKeyCode.THREE,
        "FOUR": AdaKeyCode.FOUR,
        "FIVE": AdaKeyCode.FIVE,
        "SIX": AdaKeyCode.SIX,
        "SEVEN": AdaKeyCode.SEVEN,
        "EIGHT": AdaKeyCode.EIGHT,
        "NINE": AdaKeyCode.NINE,
        "ZERO": AdaKeyCode.ZERO,
        "ENTER": AdaKeyCode.ENTER,
        "RETURN": AdaKeyCode.RETURN,
        "ESCAPE": AdaKeyCode.ESCAPE,
        "ESC": AdaKeyCode.ESCAPE,
        "BACKSPACE": AdaKeyCode.BACKSPACE,
        "BKSPC": AdaKeyCode.BACKSPACE,
        "TAB": AdaKeyCode.TAB,
        "SPACEBAR": AdaKeyCode.SPACEBAR,
        "SPACE": AdaKeyCode.SPACE,
        "MINUS": AdaKeyCode.MINUS,
        "EQUALS": AdaKeyCode.EQUALS,
        "EQ": AdaKeyCode.EQUALS,
        "LEFT_BRACKET": AdaKeyCode.LEFT_BRACKET,
        "L_BRKT": AdaKeyCode.LEFT_BRACKET,
        "RIGHT_BRACKET": AdaKeyCode.RIGHT_BRACKET,
        "R_BRKT": AdaKeyCode.RIGHT_BRACKET,
        "BACKSLASH": AdaKeyCode.BACKSLASH,
        "BKSLSH": AdaKeyCode.BACKSLASH,
        "POUND": AdaKeyCode.POUND,
        "SEMICOLON": AdaKeyCode.SEMICOLON,
        "SEMCLN": AdaKeyCode.SEMICOLON,
        "QUOTE": AdaKeyCode.QUOTE,
        "GRAVE_ACCENT": AdaKeyCode.GRAVE_ACCENT,
        "GRAVE": AdaKeyCode.GRAVE_ACCENT,
        "COMMA": AdaKeyCode.COMMA,
        "PERIOD": AdaKeyCode.PERIOD,
        "FORWARD_SLASH": AdaKeyCode.FORWARD_SLASH,
        "FWDSLSH": AdaKeyCode.FORWARD_SLASH,

        "F1": AdaKeyCode.F1,
        "F2": AdaKeyCode.F2,
        "F3": AdaKeyCode.F3,
        "F4": AdaKeyCode.F4,
        "F5": AdaKeyCode.F5,
        "F6": AdaKeyCode.F6,
        "F7": AdaKeyCode.F7,
        "F8": AdaKeyCode.F8,
        "F9": AdaKeyCode.F9,
        "F10": AdaKeyCode.F10,
        "F11": AdaKeyCode.F11,
        "F12": AdaKeyCode.F12,

        "CAPS_LOCK": AdaKeyCode.CAPS_LOCK,
        "PRINT_SCREEN": AdaKeyCode.PRINT_SCREEN,
        "SCROLL_LOCK": AdaKeyCode.SCROLL_LOCK,
        "PAUSE": AdaKeyCode.PAUSE,

        "INSERT": AdaKeyCode.INSERT,
        "HOME": AdaKeyCode.HOME,
        "PAGE_UP": AdaKeyCode.PAGE_UP,
        "DELETE": AdaKeyCode.DELETE,
        "END": AdaKeyCode.END,
        "PAGE_DOWN": AdaKeyCode.PAGE_DOWN,

        "LEFT_ARROW": AdaKeyCode.LEFT_ARROW,
        "LEFT": AdaKeyCode.LEFT_ARROW,
        "DOWN_ARROW": AdaKeyCode.DOWN_ARROW,
        "DOWN": AdaKeyCode.DOWN_ARROW,
        "UP_ARROW": AdaKeyCode.UP_ARROW,
        "UP": AdaKeyCode.UP_ARROW,

        "KEYPAD_NUMLOCK": AdaKeyCode.KEYPAD_NUMLOCK,
        "KEYPAD_FORWARD_SLASH": AdaKeyCode.KEYPAD_FORWARD_SLASH,
        "KEYPAD_ASTERISK": AdaKeyCode.KEYPAD_ASTERISK,
        "KEYPAD_MINUS": AdaKeyCode.KEYPAD_MINUS,
        "KEYPAD_PLUS": AdaKeyCode.KEYPAD_PLUS,
        "KEYPAD_ENTER": AdaKeyCode.KEYPAD_ENTER,
        "KEYPAD_ONE": AdaKeyCode.KEYPAD_ONE,
        "KEYPAD_TWO": AdaKeyCode.KEYPAD_TWO,
        "KEYPAD_THREE": AdaKeyCode.KEYPAD_THREE,
        "KEYPAD_FOUR": AdaKeyCode.KEYPAD_FOUR,
        "KEYPAD_FIVE": AdaKeyCode.KEYPAD_FIVE,
        "KEYPAD_SIX": AdaKeyCode.KEYPAD_SIX,
        "KEYPAD_SEVEN": AdaKeyCode.KEYPAD_SEVEN,
        "KEYPAD_EIGHT": AdaKeyCode.KEYPAD_EIGHT,
        "KEYPAD_NINE": AdaKeyCode.KEYPAD_NINE,
        "KEYPAD_ZERO": AdaKeyCode.KEYPAD_ZERO,
        "KEYPAD_PERIOD": AdaKeyCode.KEYPAD_PERIOD,
        "KEYPAD_BACKSLASH": AdaKeyCode.KEYPAD_BACKSLASH,
        "KEYPAD_EQUALS": AdaKeyCode.KEYPAD_EQUALS,

        "APPLICATION": AdaKeyCode.APPLICATION,
        "W_MENU": AdaKeyCode.APPLICATION,
        "POWER": AdaKeyCode.POWER,
        "MACPWR": AdaKeyCode.POWER,
        "F13": AdaKeyCode.F13,
        "F14": AdaKeyCode.F14,
        "F15": AdaKeyCode.F15,
        "F16": AdaKeyCode.F16,
        "F17": AdaKeyCode.F17,
        "F18": AdaKeyCode.F18,
        "F19": AdaKeyCode.F19,
        "F20": AdaKeyCode.F20,
        "F21": AdaKeyCode.F21,
        "F22": AdaKeyCode.F22,
        "F23": AdaKeyCode.F23,
        "F24": AdaKeyCode.F24,

        "LEFT_CONTROL": AdaKeyCode.LEFT_CONTROL,
        "CONTROL": AdaKeyCode.CONTROL,
        "CTRL": AdaKeyCode.CONTROL,
        "LEFT_SHIFT": AdaKeyCode.LEFT_SHIFT,
        "SHIFT": AdaKeyCode.SHIFT,
        "SHFT": AdaKeyCode.SHIFT,
        "LEFT_ALT": AdaKeyCode.LEFT_ALT,
        "ALT": AdaKeyCode.ALT,
        "OPTION": AdaKeyCode.OPTION,
        "LEFT_GUI": AdaKeyCode.LEFT_GUI,
        "GUI": AdaKeyCode.GUI,
        "WINDOWS": AdaKeyCode.WINDOWS,
        "WIN": AdaKeyCode.WINDOWS,
        "COMMAND": AdaKeyCode.COMMAND,
        "CMD": AdaKeyCode.COMMAND,
        "RIGHT_CONTROL": AdaKeyCode.RIGHT_CONTROL,
        "RIGHT_SHIFT": AdaKeyCode.RIGHT_SHIFT,
        "RIGHT_ALT": AdaKeyCode.RIGHT_ALT,
        "RIGHT_GUI": AdaKeyCode.RIGHT_GUI,
    }

    def factory(valueString: str):
        press = valueString[0] != "-"
        key = valueString[1:]
        value = KeyCodes.entries.get(key)
        if value == None:
            raise Exception(f"Key {key} not found in KeyCodes")

        return KeyCode(value=value, press=press, label=key)

# cspell:enable
