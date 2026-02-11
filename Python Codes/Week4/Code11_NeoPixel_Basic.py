# Import the Pin class to control ESP32 GPIO pins
from machine import Pin

# Import time module to introduce delays
import time

# Import the neopixel module to control addressable RGB LEDs
import neopixel

# Create a NeoPixel object
# GPIO pin 23 is used to control the NeoPixel data line
# There are 16 LEDs in the NeoPixel strip/ring
my_neo = neopixel.NeoPixel(Pin(23), 16)

# Set colors for individual NeoPixel LEDs
# Each LED is accessed using an index (0 to 15)
# Color format is (Red, Green, Blue) with values from 0 to 255
my_neo[0]  = (255, 0, 0)   # Red
my_neo[1]  = (0, 255, 0)   # Green
my_neo[2]  = (0, 0, 255)   # Blue
my_neo[3]  = (255, 0, 0)
my_neo[4]  = (0, 255, 0)
my_neo[5]  = (0, 0, 255)
my_neo[6]  = (255, 0, 0)
my_neo[7]  = (0, 255, 0)
my_neo[8]  = (0, 0, 255)
my_neo[9]  = (255, 0, 0)
my_neo[10] = (0, 255, 0)
my_neo[11] = (0, 0, 255)
my_neo[12] = (255, 0, 0)
my_neo[13] = (0, 255, 0)
my_neo[14] = (0, 0, 255)
my_neo[15] = (255, 0, 0)

# Send the color data to the NeoPixel LEDs
# Changes will not appear until write() is called
my_neo.write()

# Keep the LEDs ON for 2 seconds
time.sleep(2)

# Turn OFF all NeoPixel LEDs by setting color to (0, 0, 0)
my_neo[0]  = (0, 0, 0)
my_neo[1]  = (0, 0, 0)
my_neo[2]  = (0, 0, 0)
my_neo[3]  = (0, 0, 0)
my_neo[4]  = (0, 0, 0)
my_neo[5]  = (0, 0, 0)
my_neo[6]  = (0, 0, 0)
my_neo[7]  = (0, 0, 0)
my_neo[8]  = (0, 0, 0)
my_neo[9]  = (0, 0, 0)
my_neo[10] = (0, 0, 0)
my_neo[11] = (0, 0, 0)
my_neo[12] = (0, 0, 0)
my_neo[13] = (0, 0, 0)
my_neo[14] = (0, 0, 0)
my_neo[15] = (0, 0, 0)

# Update the NeoPixels to turn them OFF
my_neo.write()

# Keep the LEDs OFF for 2 seconds
time.sleep(2)
