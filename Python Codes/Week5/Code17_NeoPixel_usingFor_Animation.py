# Import Pin class to control ESP32 GPIO pins
from machine import Pin

# Import neopixel library to control NeoPixel LEDs
import neopixel

# Import time module for delays
import time

# Create a NeoPixel object
# Pin(23)  → Data pin connected to NeoPixel
# 16      → Number of LEDs in the ring/strip
my_neo = neopixel.NeoPixel(Pin(23), 16)

# Infinite loop so the animation runs continuously
while True:
    
    # FOR loop to turn ON LEDs one by one
    # range(0,16) means LED index from 0 to 15
    for iteration in range(0,16):
        
        # Set the current LED color to RED
        # (255, 0, 0) → Red, Green, Blue
        my_neo[iteration] = (255, 0, 0)
        
        # Send the updated color data to the NeoPixel LEDs
        my_neo.write()
        
        # Small delay to create animation effect
        time.sleep(0.1)
    
    # FOR loop to turn OFF LEDs one by one
    for num in range(0,16):
        
        # Turn OFF the current LED
        # (0, 0, 0) means no light
        my_neo[num] = (0, 0, 0)
        
        # Update the LEDs with new values
        my_neo.write()
        
        # Delay for visible OFF animation
        time.sleep(0.1)
