# Sand Piper

Custom CircuitPython hotkey & macro pad firmware for the **Adafruit MacroPad RP2040**, featuring on-device configuration menus and non-volatile memory (`microcontroller.nvm`) persistence powered by [`mgogo`](https://github.com/calbert1209/mgogo).

---

## Features

- **Multi-Page 3×4 Hotkey Grid**: Organize macros across multiple pages and switch between them with the rotary encoder.
- **Per-Key RGB Colors & Labels**: Each key (`0..11`) has a custom 7-character OLED label, custom 24-bit RGB NeoPixel color, and a sequence of USB HID key press/release actions.
- **On-Device Settings Editor**: Edit key labels, RGB LED colors, keystroke chords, and page titles—or add and delete pages—directly on the MacroPad without touching code.
- **Non-Volatile Storage (`microcontroller.nvm`)**: Saves all pages and key configurations directly to the RP2040's built-in non-volatile memory using `mgogo` binary serialization (no need to disable the `CIRCUITPY` USB drive).

---

## Hardware & Requirements

- **Board**: [Adafruit MacroPad RP2040](https://www.adafruit.com/product/5128)
- **Firmware**: CircuitPython 9.x
- **Libraries** (bundled in [`lib/`](file:///Users/albert/Projects/sand_piper/lib)):
  - `adafruit_macropad`
  - `adafruit_display_text`
  - `adafruit_display_shapes`
  - `adafruit_bitmap_font`
  - `adafruit_hid`
  - `adafruit_midi`
  - `adafruit_debouncer`
  - `adafruit_simple_text_display`
  - `adafruit_ticks`
  - `neopixel`

---

## Deploying to Your MacroPad

1. Connect the MacroPad RP2040 via USB so that it mounts at `/Volumes/CIRCUITPY`.
2. Run the sync command from the project root:
   ```bash
   make sync
   ```
   This runs [`send_to.sh`](file:///Users/albert/Projects/sand_piper/send_to.sh) using `rsync` (respecting [`.rsyncignore`](file:///Users/albert/Projects/sand_piper/.rsyncignore)) to copy the firmware and libraries to `/Volumes/CIRCUITPY`.

---

## Usage Guide

### 1. Normal Hotkey Mode
When the MacroPad boots normally (without holding the rotary encoder button):
- **Switch Pages**: Turn the rotary encoder clockwise or counter-clockwise.
- **Trigger Macros**: Press any key (`0..11`) on the 3×4 keypad. The key's LED flashes white while pressed and sends its configured USB HID keystroke sequence.

### 2. Settings Mode
To enter **Settings Mode**, **hold down the rotary encoder button while booting or resetting** the MacroPad.

The OLED header displays `*<PAGE NAME>*` to indicate Settings Mode is active, starting on the first page of keys.

#### Editing a Key
1. Rotate the encoder to navigate to the desired page.
2. Press any key (`0..11`) on the 3×4 grid to open its **Key Settings Menu**:
   - **Key 0 (`label`)**: Select label option, then press **Key 11 (`OK`)** to edit the key's display name (up to 7 characters). Rotate the encoder to browse characters, press **Keys 0..8** to type, **Key 10 (`DEL`)** to backspace, **Key 9 (`BACK`)** to cancel, or **Key 11 (`OK`)** to confirm.
   - **Key 3 (`color`)**: Select color option, then press **Key 11 (`OK`)** to adjust Red (`Key 6`), Green (`Key 7`), and Blue (`Key 8`) values (`0..255`) using the rotary encoder.
   - **Key 6 (`codes`)**: Select keycodes option, then press **Key 11 (`OK`)** to build a keystroke chord. Press the rotary encoder button to toggle between key press (`+`) and key release (`-`), rotate the encoder to browse keys, press **Keys 0..8** to append a keycode, **Key 10 (`DEL`)** to remove the last keycode, or **Key 11 (`OK`)** to confirm.
3. Press **Key 9 (`BACK`)** in the Key Settings Menu to return to the 3×4 Settings Grid.

#### Renaming or Deleting a Page
1. While on a page in the 3×4 Settings Grid, **short-press the rotary encoder button** to open the **Page Menu**:
   - **`> title`**: Press **Key 0** (or rotate encoder) and press **Key 11 (`OK`)** to rename the page (up to 15 characters).
   - **`> delete page`**: Press **Key 3** (or rotate encoder) and press **Key 11 (`OK`)** to delete the current page (available whenever more than 1 page exists).
   - Press **Key 9 (`BACK`)** to return to the 3×4 Settings Grid.

#### Adding a New Page
1. In the 3×4 Settings Grid, rotate the encoder past the last page to reach the **`+ ADD PAGE +`** screen.
2. Press any key (or short-press the rotary encoder button) to create a new blank page and immediately set its title.

#### Saving & Rebooting
- From the 3×4 Settings Grid, **long-press (hold for ~1 second) the rotary encoder button**.
- All pages and key settings are serialized via `mgogo` into `microcontroller.nvm`, and the MacroPad automatically reboots into Normal Hotkey Mode.
