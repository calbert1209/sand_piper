# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# HINT
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage

"""CircuitPython Essentials Storage logging example"""
import time
import board
import digitalio
import microcontroller
import storage

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()
count = 0

try:
    with open("/temperature.txt", "a") as fp:
        while count < 20:
            temp = microcontroller.cpu.temperature
            # do the C-to-F conversion here if you would like
            print(f"{count + 1}: {temp:02f}")
            fp.write('{0:f}\n'.format(temp))
            fp.flush()
            led.value = not led.value
            time.sleep(1)
            count += 1
except OSError as e:  # Typically when the filesystem isn't writeable...
    delay = 0.5  # ...blink the LED every half second.
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.25  # ...blink the LED faster!
    while True:
        led.value = not led.value
        time.sleep(delay)
finally:
    if count >= 20:
        print("success, enabling usb_drive")
        storage.enable_usb_drive()
