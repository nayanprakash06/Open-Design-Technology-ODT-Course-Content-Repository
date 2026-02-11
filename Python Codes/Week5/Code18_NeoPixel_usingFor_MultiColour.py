# Import Pin class to control ESP32 GPIO pins
from machine import Pin

# Import neopixel library to control NeoPixel LEDs
import neopixel

# Import time module for delays
import time

# (IMPORTANT) random module is needed for random colors
import random

# Create NeoPixel object
# Pin(23)  → Data pin connected to NeoPixel
# 16      → Total number of LEDs
my_neo = neopixel.NeoPixel(Pin(23), 16)

# Infinite loop so animation keeps running
while True:
    
    # Generate random RED value between 150 and 255
    # High values ensure bright colors
    r = random.randint(150, 255)
    
    # Generate random GREEN value
    g = random.randint(150, 255)
    
    # Generate random BLUE value
    b = random.randint(150, 255)
    
    # FOR loop to turn ON LEDs one by one
    # iteration and num are just index variables
    for iteration in range(0, 16):
        
        # Set current LED to the randomly generated color
        my_neo[iteration] = (r, g, b)
        
        # Update the NeoPixel LEDs
        my_neo.write()
        
        # Delay to create chasing animation
        time.sleep(0.1)
    
    # FOR loop to turn OFF LEDs one by one
    for num in range(0, 16):
        
        # Turn OFF current LED
        my_neo[num] = (0, 0, 0)
        
        # Update LEDs
        my_neo.write()
        
        # Delay for OFF animation
        time.sleep(0.1)
