# Import the Pin class to control the ESP32 GPIO pins
from machine import Pin

# Import the time module to use delay functions
import time

# Create a Pin object named my_led
# GPIO pin 4 is configured as an OUTPUT pin to control an LED
my_led = Pin(22, Pin.OUT)

# Start an infinite loop
# while True means the loop will run forever unless the board is reset
while True:

    # Turn the LED ON by setting the pin to HIGH
    my_led.on()

    # Keep the LED ON for 0.5 seconds
    time.sleep(0.5)

    # Turn the LED OFF by setting the pin to LOW
    my_led.off()

    # Keep the LED OFF for 0.5 seconds
    time.sleep(0.5)
