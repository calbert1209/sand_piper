# AGENTS.md

Guidance for AI coding agents working in the `sand_piper` repository.

---

## Project Overview

`sand_piper` is a CircuitPython 9.x firmware for the **Adafruit MacroPad RP2040** (`128x64` monochrome SH1106 OLED, `3x4` mechanical key matrix with per-key RGB NeoPixels, and rotary encoder with push switch).

It implements a multi-page USB HID hotkey pad with an on-device MVVM menu system for editing key labels, LED colors, keystroke chords, and pages, backed by binary serialization to `microcontroller.nvm` via [`mgogo`](https://github.com/calbert1209/mgogo).

---

## Repository Structure

```text
.
├── boot.py                     # CircuitPython boot script
├── code.py                     # Main application entrypoint & state router
├── Makefile                    # `make sync` target to deploy to /Volumes/CIRCUITPY
├── send_to.sh                  # rsync deployment script for FAT filesystems
├── .rsyncignore                # Files/folders excluded from syncing to CIRCUITPY
├── lib/                        # Pre-compiled CircuitPython (.mpy) libraries
└── sand_piper/
    ├── EventBus.py             # Polls MacroPad keys/encoder and dispatches HidEvents
    ├── PaginationManager.py    # Helper for paginating option lists across the 3x3 grid
    ├── Storage.py              # microcontroller.nvm load/save + default fallback pages
    ├── Models/
    │   ├── Keycodes.py         # KeyCode model & mapping to adafruit_hid.keycode.Keycode
    │   ├── Mgogo.py            # Inlined binary serializer/deserializer (from calbert1209/mgogo)
    │   ├── Model.py            # KeySettings and ControlPage domain models
    │   └── RgbValue.py         # Clamped (0..255) RGB color model
    └── Pages/
        ├── KeyGrid/            # Main 3x4 hotkey grid + Settings Mode grid + "+ ADD PAGE +"
        ├── EditPage/           # Page-level menu (rename page title, delete page)
        ├── EditSettings/       # Key-level menu (select label, color, or keyCodes)
        ├── EditLabel/          # 3x3 paginated character picker for key/page labels
        ├── EditColor/          # R/G/B rotary encoder color editor with live LED preview
        └── EditKeyCodes/       # 3x3 paginated keycode chord builder (+press / -release)
```

---

## Architecture & Conventions

### 1. CircuitPython Runtime Constraints
- **Python Compatibility**: Avoid Python 3.10+ runtime union syntax (e.g., `str | None` or `list[int] | None`) in function signatures or class attributes evaluated at import time, as CircuitPython's MicroPython core and older host Python runtimes may raise `TypeError: unsupported operand type(s) for |`.
- **Import Casing**: The `CIRCUITPY` FAT filesystem and case-sensitive tools require exact filename casing in imports. Notably, use `from sand_piper.Models.Keycodes import ...` (lowercase `c` in `Keycodes.py`).
- **Display & NeoPixel Refresh**:
  - `macroPad.display.auto_refresh` and `macroPad.pixels.auto_write` are set to `False`.
  - Always call `self._view.show()` (`macroPad.display.refresh()`) and `self._pixels.show()` explicitly after updating UI text or LEDs.

### 2. MVVM Page Pattern (`sand_piper/Pages/<PageName>/`)
Each screen is split into a `Display` and a `ViewModel`:
- **`Display.py`**: Builds a `displayio.Group` and exposes methods like `setText(i, value)`, `setTitle(value)`, and `show()`.
- **`ViewModel.py`**:
  - `connect(self, macroPad: MacroPad, eventBus: EventBus)`: Binds `macroPad.display.root_group = self._view.group`, initializes LEDs, and registers event handlers on `eventBus`.
  - `update(self)`: Called once per main loop tick in `code.py`.
  - `disconnect(self)`: Clears LEDs/keys and releases references before route transitions (`eventBus.requestReset()` clears all `EventBus` callbacks).

### 3. `Mgogo` Binary Format (`sand_piper/Models/Mgogo.py`)
`Mgogo.py` is an inlined distribution of [`calbert1209/mgogo`](https://github.com/calbert1209/mgogo):
- **Prefixes**:
  - `#` (`ShortWord`, 4 bytes): `#` + 3 raw RGB bytes
  - `_` (`Word`, 8 bytes): `_` + 7 space-padded ASCII chars (key label)
  - `$` (`LongWord`, 16 bytes): `$` + 15 space-padded ASCII chars (page title)
  - `+` (`PushCode`, 2 bytes): `+` + 1 raw keycode byte
  - `-` (`ReleaseCode`, 2 bytes): `-` + 1 raw keycode byte
  - `*` (`Array`): `*` + 1 length byte + concatenated item bytes
  - `<` (`KeyCommand`): `<` + `Word` + `ShortWord` + `Array[PushCode | ReleaseCode]`
  - `[` (`PadPage`): `[` + `LongWord` + `Array[KeyCommand]`
  - `\n` (`END`): Terminates serialized payload in `microcontroller.nvm`
- If you modify `sand_piper/Models/Mgogo.py`, ensure changes remain compatible with the upstream [`calbert1209/mgogo`](https://github.com/calbert1209/mgogo) repository.

---

## Development & Verification Workflow

### Syncing to Hardware
- Always keep non-device files (e.g., `README.md`, `AGENTS.md`, `.agent/`, `.git/`, `.vscode/`, `Makefile`, `send_to.sh`, `requirements.txt`) listed in [`.rsyncignore`](file:///Users/albert/Projects/sand_piper/.rsyncignore) so `make sync` does not copy them onto the microcontroller's small flash drive or delete CircuitPython system files (`boot_out.txt`, `sd/`, `.fseventsd/`).
- Deploy to a mounted `/Volumes/CIRCUITPY` drive with:
  ```bash
  make sync
  ```

### Running Host-Side Checks
Before syncing to `/Volumes/CIRCUITPY`:
1. **Syntax & Compile Check** (and clean up `__pycache__` afterward so bytecode isn't synced to the device):
   ```bash
   python3 -m py_compile code.py boot.py sand_piper/*.py sand_piper/Models/*.py sand_piper/Pages/*/*.py
   find . -name "__pycache__" -exec rm -rf {} +
   ```
2. **Serialization Round-Trip Test**:
   Test `encodePages()` and `decodePages()` in `sand_piper/Storage.py` with a mocked `adafruit_hid.keycode` module on the host machine to verify lossless binary serialization.
