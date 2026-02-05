# Import Pin and TouchPad classes from the machine module
# Pin is used to select a GPIO pin
# TouchPad is used to read capacitive touch values on ESP32
from machine import Pin, TouchPad

# Import time module to add delays in the program
import time

# Create a TouchPad object using GPIO pin 4
# This pin will act as a capacitive touch sensor
my_touch_pin = TouchPad(Pin(4))

# Start an infinite loop
# The code inside this loop will run continuously
while True:

    # Read the current touch sensor value
    # Lower values usually indicate that the pin is being touched
    touch_pin_values = my_touch_pin.read()

    # Print the touch sensor value on the serial console
    print(touch_pin_values)

    # Wait for 0.2 seconds before taking the next reading
    time.sleep(0.2)
