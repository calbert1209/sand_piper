from adafruit_hid.keycode import Keycode as AdaKeyCode

# cspell:disable


class KeyCodes:
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
        # "RIGHT_ARROW",
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

        "RIGHT_ARROW": AdaKeyCode.RIGHT_ARROW,
        "RIGHT": AdaKeyCode.RIGHT_ARROW,
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

    A = 0x04
    """``a`` and ``A``"""
    B = 0x05
    """``b`` and ``B``"""
    C = 0x06
    """``c`` and ``C``"""
    D = 0x07
    """``d`` and ``D``"""
    E = 0x08
    """``e`` and ``E``"""
    F = 0x09
    """``f`` and ``F``"""
    G = 0x0A
    """``g`` and ``G``"""
    H = 0x0B
    """``h`` and ``H``"""
    I = 0x0C
    """``i`` and ``I``"""
    J = 0x0D
    """``j`` and ``J``"""
    K = 0x0E
    """``k`` and ``K``"""
    L = 0x0F
    """``l`` and ``L``"""
    M = 0x10
    """``m`` and ``M``"""
    N = 0x11
    """``n`` and ``N``"""
    O = 0x12
    """``o`` and ``O``"""
    P = 0x13
    """``p`` and ``P``"""
    Q = 0x14
    """``q`` and ``Q``"""
    R = 0x15
    """``r`` and ``R``"""
    S = 0x16
    """``s`` and ``S``"""
    T = 0x17
    """``t`` and ``T``"""
    U = 0x18
    """``u`` and ``U``"""
    V = 0x19
    """``v`` and ``V``"""
    W = 0x1A
    """``w`` and ``W``"""
    X = 0x1B
    """``x`` and ``X``"""
    Y = 0x1C
    """``y`` and ``Y``"""
    Z = 0x1D
    """``z`` and ``Z``"""

    ONE = 0x1E
    """``1`` and ``!``"""
    TWO = 0x1F
    """``2`` and ``@``"""
    THREE = 0x20
    """``3`` and ``#``"""
    FOUR = 0x21
    """``4`` and ``$``"""
    FIVE = 0x22
    """``5`` and ``%``"""
    SIX = 0x23
    """``6`` and ``^``"""
    SEVEN = 0x24
    """``7`` and ``&``"""
    EIGHT = 0x25
    """``8`` and ``*``"""
    NINE = 0x26
    """``9`` and ``(``"""
    ZERO = 0x27
    """``0`` and ``)``"""
    ENTER = 0x28
    """Enter (Return)"""
    RETURN = ENTER
    """Alias for ``ENTER``"""
    ESCAPE = 0x29
    """Escape"""
    BACKSPACE = 0x2A
    """Delete backward (Backspace)"""
    TAB = 0x2B
    """Tab and Backtab"""
    SPACEBAR = 0x2C
    """Spacebar"""
    SPACE = SPACEBAR
    """Alias for SPACEBAR"""
    MINUS = 0x2D
    """``-` and ``_``"""
    EQUALS = 0x2E
    """``=` and ``+``"""
    LEFT_BRACKET = 0x2F
    """``[`` and ``{``"""
    RIGHT_BRACKET = 0x30
    """``]`` and ``}``"""
    BACKSLASH = 0x31
    r"""``\`` and ``|``"""
    POUND = 0x32
    """``#`` and ``~`` (Non-US keyboard)"""
    SEMICOLON = 0x33
    """``;`` and ``:``"""
    QUOTE = 0x34
    """``'`` and ``"``"""
    GRAVE_ACCENT = 0x35
    r""":literal:`\`` and ``~``"""
    COMMA = 0x36
    """``,`` and ``<``"""
    PERIOD = 0x37
    """``.`` and ``>``"""
    FORWARD_SLASH = 0x38
    """``/`` and ``?``"""

    CAPS_LOCK = 0x39
    """Caps Lock"""

    F1 = 0x3A
    """Function key F1"""
    F2 = 0x3B
    """Function key F2"""
    F3 = 0x3C
    """Function key F3"""
    F4 = 0x3D
    """Function key F4"""
    F5 = 0x3E
    """Function key F5"""
    F6 = 0x3F
    """Function key F6"""
    F7 = 0x40
    """Function key F7"""
    F8 = 0x41
    """Function key F8"""
    F9 = 0x42
    """Function key F9"""
    F10 = 0x43
    """Function key F10"""
    F11 = 0x44
    """Function key F11"""
    F12 = 0x45
    """Function key F12"""

    PRINT_SCREEN = 0x46
    """Print Screen (SysRq)"""
    SCROLL_LOCK = 0x47
    """Scroll Lock"""
    PAUSE = 0x48
    """Pause (Break)"""

    INSERT = 0x49
    """Insert"""
    HOME = 0x4A
    """Home (often moves to beginning of line)"""
    PAGE_UP = 0x4B
    """Go back one page"""
    DELETE = 0x4C
    """Delete forward"""
    END = 0x4D
    """End (often moves to end of line)"""
    PAGE_DOWN = 0x4E
    """Go forward one page"""

    RIGHT_ARROW = 0x4F
    """Move the cursor right"""
    LEFT_ARROW = 0x50
    """Move the cursor left"""
    DOWN_ARROW = 0x51
    """Move the cursor down"""
    UP_ARROW = 0x52
    """Move the cursor up"""

    KEYPAD_NUMLOCK = 0x53
    """Num Lock (Clear on Mac)"""
    KEYPAD_FORWARD_SLASH = 0x54
    """Keypad ``/``"""
    KEYPAD_ASTERISK = 0x55
    """Keypad ``*``"""
    KEYPAD_MINUS = 0x56
    """Keyapd ``-``"""
    KEYPAD_PLUS = 0x57
    """Keypad ``+``"""
    KEYPAD_ENTER = 0x58
    """Keypad Enter"""
    KEYPAD_ONE = 0x59
    """Keypad ``1`` and End"""
    KEYPAD_TWO = 0x5A
    """Keypad ``2`` and Down Arrow"""
    KEYPAD_THREE = 0x5B
    """Keypad ``3`` and PgDn"""
    KEYPAD_FOUR = 0x5C
    """Keypad ``4`` and Left Arrow"""
    KEYPAD_FIVE = 0x5D
    """Keypad ``5``"""
    KEYPAD_SIX = 0x5E
    """Keypad ``6`` and Right Arrow"""
    KEYPAD_SEVEN = 0x5F
    """Keypad ``7`` and Home"""
    KEYPAD_EIGHT = 0x60
    """Keypad ``8`` and Up Arrow"""
    KEYPAD_NINE = 0x61
    """Keypad ``9`` and PgUp"""
    KEYPAD_ZERO = 0x62
    """Keypad ``0`` and Ins"""
    KEYPAD_PERIOD = 0x63
    """Keypad ``.`` and Del"""
    KEYPAD_BACKSLASH = 0x64
    """Keypad ``\\`` and ``|`` (Non-US)"""

    APPLICATION = 0x65
    """Application: also known as the Menu key (Windows)"""
    POWER = 0x66
    """Power (Mac)"""
    KEYPAD_EQUALS = 0x67
    """Keypad ``=`` (Mac)"""
    F13 = 0x68
    """Function key F13 (Mac)"""
    F14 = 0x69
    """Function key F14 (Mac)"""
    F15 = 0x6A
    """Function key F15 (Mac)"""
    F16 = 0x6B
    """Function key F16 (Mac)"""
    F17 = 0x6C
    """Function key F17 (Mac)"""
    F18 = 0x6D
    """Function key F18 (Mac)"""
    F19 = 0x6E
    """Function key F19 (Mac)"""

    F20 = 0x6F
    """Function key F20"""
    F21 = 0x70
    """Function key F21"""
    F22 = 0x71
    """Function key F22"""
    F23 = 0x72
    """Function key F23"""
    F24 = 0x73
    """Function key F24"""

    LEFT_CONTROL = 0xE0
    """Control modifier left of the spacebar"""
    CONTROL = LEFT_CONTROL
    """Alias for LEFT_CONTROL"""
    LEFT_SHIFT = 0xE1
    """Shift modifier left of the spacebar"""
    SHIFT = LEFT_SHIFT
    """Alias for LEFT_SHIFT"""
    LEFT_ALT = 0xE2
    """Alt modifier left of the spacebar"""
    ALT = LEFT_ALT
    """Alias for LEFT_ALT; Alt is also known as Option (Mac)"""
    OPTION = ALT
    """Labeled as Option on some Mac keyboards"""
    LEFT_GUI = 0xE3
    """GUI modifier left of the spacebar"""
    GUI = LEFT_GUI
    """Alias for LEFT_GUI; GUI is also known as the Windows key, Command (Mac), or Meta"""
    WINDOWS = GUI
    """Labeled with a Windows logo on Windows keyboards"""
    COMMAND = GUI
    """Labeled as Command on Mac keyboards, with a clover glyph"""
    RIGHT_CONTROL = 0xE4
    """Control modifier right of the spacebar"""
    RIGHT_SHIFT = 0xE5
    """Shift modifier right of the spacebar"""
    RIGHT_ALT = 0xE6
    """Alt modifier right of the spacebar"""
    RIGHT_GUI = 0xE7
    """GUI modifier right of the spacebar"""

# cspell:enable
