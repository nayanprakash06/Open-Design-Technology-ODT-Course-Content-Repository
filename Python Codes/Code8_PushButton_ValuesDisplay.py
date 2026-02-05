# Import the Pin class to work with ESP32 GPIO pins
from machine import Pin

# Import time module to add delays in the program
import time

# Create a Pin object for the push button
# GPIO pin 22 is configured as an INPUT pin
# Internal PULL_UP resistor is enabled
# When the button is NOT pressed → value is 1 (HIGH)
# When the button IS pressed → value is 0 (LOW)
my_Push_Button = Pin(22, Pin.IN, Pin.PULL_UP)

# Start an infinite loop
# The program continuously checks the button state
while True:

    # Read the current logic level of the push button
    # Returns 1 if not pressed, 0 if pressed
    Push_Button_values = my_Push_Button.value()

    # Print the button value on the serial console
    # This helps in monitoring button press and release
    print(Push_Button_values)

    # Wait for 0.2 seconds before the next reading
    time.sleep(0.2)
