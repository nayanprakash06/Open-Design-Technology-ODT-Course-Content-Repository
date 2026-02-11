# Import the Pin class to control GPIO pins of the ESP32
from machine import Pin

# Import the time module to introduce delays in the program
import time

# Create a Pin object for the first LED
# GPIO pin 22 is configured as an OUTPUT pin
my_led_1 = Pin(22, Pin.OUT)

# Create a Pin object for the second LED
# GPIO pin 23 is configured as an OUTPUT pin
my_led_2 = Pin(23, Pin.OUT)

# Start an infinite loop
# The code inside this loop will keep running continuously
while True:

    # Turn ON LED 1
    # Turn OFF LED 2
    my_led_1.on()
    my_led_2.off()

    # Wait for 0.5 seconds
    time.sleep(0.5)

    # Turn OFF LED 1
    # Turn ON LED 2
    my_led_1.off()
    my_led_2.on()

    # Wait for 0.5 seconds
    time.sleep(0.5)
