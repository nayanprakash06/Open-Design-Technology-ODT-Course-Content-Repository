# Import the Pin class from the machine module
# Pin allows us to control the ESP32's GPIO pins
from machine import Pin

# Create a Pin object named my_led
# GPIO pin 22 is selected and configured as an OUTPUT pin
# This means it can send HIGH or LOW signals (used to control an LED)
my_led = Pin(22, Pin.OUT)

# Set the GPIO pin HIGH
# This turns the LED ON (assuming the LED is connected correctly, LED's + to GPIO 22)
my_led.on()
