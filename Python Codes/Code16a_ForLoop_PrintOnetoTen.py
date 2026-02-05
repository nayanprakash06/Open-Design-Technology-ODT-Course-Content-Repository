# Import the Pin class to control ESP32 GPIO pins
from machine import Pin

# Import neopixel module to control addressable RGB LEDs
import neopixel

# Import time module to introduce delays
import time

# Create a NeoPixel object
# GPIO pin 23 is used as the data pin
# 16 NeoPixel LEDs are connected
my_neo = neopixel.NeoPixel(Pin(23), 16)

# Start an infinite loop
# The LED pattern will repeat continuously
while True:

    # -------- TURN ALL LEDs ON --------

    # Loop through LED indices from 0 to 15
    for iteration in range(0, 16):
        # Set each LED color to RED
        my_neo[iteration] = (255, 0, 0)

    # Send the updated color data to the NeoPixels
    my_neo.write()

    # Keep all LEDs ON for 2 seconds
    time.sleep(2)

    # -------- TURN ALL LEDs OFF --------

    # Loop through LED indices from 0 to 15
    for num in range(0, 16):
        # Turn OFF each LED by setting color to (0, 0, 0)
        my_neo[num] = (0, 0, 0)

    # Update the NeoPixels to apply the OFF state
    my_neo.write()

    # Keep all LEDs OFF for 1 second
    time.sleep(1)
