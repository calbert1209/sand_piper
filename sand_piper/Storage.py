from sand_piper.Models.Keycodes import KeyCodes
from sand_piper.Models.Mgogo import Array, Decoder, Encoder, PadPage
from sand_piper.Models.Model import ControlPage, KeySettings
from sand_piper.Models.RgbValue import RGBValue


def _makeKey(label: str, r: int, g: int, b: int, codes: list[str]) -> KeySettings:
    return KeySettings(
        label=label,
        color=RGBValue(r, g, b),
        keyCodes=[KeyCodes.factory(c) for c in codes],
    )


def getDefaultPages() -> list[ControlPage]:
    return [
        ControlPage(
            "HOTKEYS 1",
            [
                _makeKey("COPY", 255, 128, 0, ["+CMD", "+C"]),
                _makeKey("PASTE", 0, 255, 0, ["+CMD", "+V"]),
                _makeKey("CUT", 0, 128, 255, ["+CMD", "+X"]),
                _makeKey("UNDO", 255, 0, 128, ["+CMD", "+Z"]),
                _makeKey("REDO", 128, 0, 255, ["+CMD", "+SHFT", "+Z"]),
                _makeKey("SAVE", 0, 255, 128, ["+CMD", "+S"]),
                _makeKey("FIND", 255, 255, 0, ["+CMD", "+F"]),
                _makeKey("ALL", 128, 255, 0, ["+CMD", "+A"]),
                _makeKey("TAB", 0, 255, 255, ["+CMD", "+T"]),
                _makeKey("CLOSE", 255, 0, 0, ["+CMD", "+W"]),
                _makeKey("SWITCH", 128, 128, 255, ["+CMD", "+TAB"]),
                _makeKey("ENTER", 0, 200, 64, ["+ENTER"]),
            ],
        ),
        ControlPage(
            "HOTKEYS 2",
            [
                _makeKey("ONE", 255, 64, 0, ["+ONE"]),
                _makeKey("TWO", 255, 128, 0, ["+TWO"]),
                _makeKey("THREE", 255, 255, 0, ["+THREE"]),
                _makeKey("FOUR", 0, 255, 0, ["+FOUR"]),
                _makeKey("FIVE", 0, 255, 128, ["+FIVE"]),
                _makeKey("SIX", 0, 255, 255, ["+SIX"]),
                _makeKey("SEVEN", 0, 128, 255, ["+SEVEN"]),
                _makeKey("EIGHT", 0, 0, 255, ["+EIGHT"]),
                _makeKey("NINE", 128, 0, 255, ["+NINE"]),
                _makeKey("LEFT", 255, 0, 128, ["+LEFT"]),
                _makeKey("ZERO", 128, 128, 128, ["+ZERO"]),
                _makeKey("RIGHT", 255, 0, 64, ["+RIGHT"]),
            ],
        ),
    ]


def encodePages(pages: list[ControlPage]) -> bytes:
    padPages = [p.toMgogo() for p in pages]
    rootArray = Array(len(padPages), padPages)
    return Encoder.encode(rootArray)


def decodePages(rawData: bytes) -> list[ControlPage]:
    decoder = Decoder()
    trimmed = decoder.trim(rawData)
    if len(trimmed) == 0:
        raise ValueError("Empty NVM data")

    decoded = decoder.decode(trimmed)
    if isinstance(decoded, PadPage):
        return [ControlPage.fromMgogo(decoded)]
    if isinstance(decoded, Array):
        pages = [ControlPage.fromMgogo(p) for p in decoded.items]
        if len(pages) == 0:
            raise ValueError("No pages found in NVM data")
        return pages

    raise ValueError("Unexpected root type in NVM data")


def loadPagesFromNvm() -> list[ControlPage]:
    try:
        import microcontroller

        if microcontroller.nvm is not None and len(microcontroller.nvm) > 0:
            return decodePages(microcontroller.nvm[:])
    except Exception as err:
        print("Using default settings (NVM load failed):", err)

    return getDefaultPages()


def savePagesToNvm(pages: list[ControlPage]) -> bool:
    try:
        import microcontroller

        data = encodePages(pages)
        if microcontroller.nvm is None:
            print("microcontroller.nvm is not available")
            return False
        if len(data) > len(microcontroller.nvm):
            raise ValueError(
                f"Encoded settings ({len(data)} bytes) exceed NVM size ({len(microcontroller.nvm)} bytes)"
            )
        microcontroller.nvm[0 : len(data)] = data
        return True
    except Exception as err:
        print("Failed to save settings to NVM:", err)
        return False

