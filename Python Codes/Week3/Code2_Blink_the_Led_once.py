# Import the Pin class from the machine module
# This is used to control GPIO pins of the ESP32
from machine import Pin

# Import the time module
# This allows us to introduce delays in the program
import time

# Create a Pin object named my_led
# GPIO pin 22 is configured as an OUTPUT pin to control an LED
my_led = Pin(22, Pin.OUT)

# Turn the LED ON by setting the pin to logic HIGH
my_led.on()

# Pause the program execution for 0.5 seconds
# The LED remains ON during this time
time.sleep(0.5)

# Turn the LED OFF by setting the pin to logic LOW
my_led.off()

# Pause the program execution for 0.5 seconds
# The LED remains OFF during this time
time.sleep(0.5)
