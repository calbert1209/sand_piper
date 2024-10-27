# This example is for the MacroPad,
# or any board with buttons that are connected to ground when pressed.

import board
import digitalio
import storage
import time

# On the Macropad, pressing a key grounds it. You need to set a pull-up.
# If not pressed, the key will be at +V (due to the pull-up).
button = digitalio.DigitalInOut(board.KEY5)
button.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
msg = "Key 5 pressed" if not button.value else "No press"

print(msg)
time.sleep(1.0)

# if not button.value:
#     storage.disable_usb_drive()
