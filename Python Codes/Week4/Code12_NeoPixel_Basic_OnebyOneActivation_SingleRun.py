# Import the Pin class to control ESP32 GPIO pins
from machine import Pin

# Import time module to introduce delays
import time

# Import neopixel module to control addressable RGB LEDs
import neopixel

# Create a NeoPixel object
# GPIO pin 23 is used as the data pin
# There are 16 NeoPixel LEDs connected
my_neo = neopixel.NeoPixel(Pin(23), 16)

# -------- TURNING LEDs ON ONE BY ONE --------

# Turn ON NeoPixel at index 0 with RED color
my_neo[0] = (255, 0, 0)
my_neo.write()        # Send data to the LEDs
time.sleep(0.2)       # Small delay to see the effect

# Turn ON NeoPixel at index 1 with GREEN color
my_neo[1] = (0, 255, 0)
my_neo.write()
time.sleep(0.2)

# Turn ON NeoPixel at index 2 with BLUE color
my_neo[2] = (0, 0, 255)
my_neo.write()
time.sleep(0.2)

# Continue turning ON LEDs one by one with repeating colors
my_neo[3] = (255, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[4] = (0, 255, 0)
my_neo.write()
time.sleep(0.2)

my_neo[5] = (0, 0, 255)
my_neo.write()
time.sleep(0.2)

my_neo[6] = (255, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[7] = (0, 255, 0)
my_neo.write()
time.sleep(0.2)

my_neo[8] = (0, 0, 255)
my_neo.write()
time.sleep(0.2)

my_neo[9] = (255, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[10] = (0, 255, 0)
my_neo.write()
time.sleep(0.2)

my_neo[11] = (0, 0, 255)
my_neo.write()
time.sleep(0.2)

my_neo[12] = (255, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[13] = (0, 255, 0)
my_neo.write()
time.sleep(0.2)

my_neo[14] = (0, 0, 255)
my_neo.write()
time.sleep(0.2)

my_neo[15] = (255, 0, 0)
my_neo.write()
time.sleep(0.2)

# -------- TURNING LEDs OFF ONE BY ONE --------

# Turn OFF NeoPixel at index 0
my_neo[0] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

# Turn OFF NeoPixel at index 1
my_neo[1] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

# Continue turning OFF LEDs one by one
my_neo[2] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[3] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[4] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[5] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[6] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[7] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[8] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[9] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[10] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[11] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[12] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[13] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[14] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)

my_neo[15] = (0, 0, 0)
my_neo.write()
time.sleep(0.2)