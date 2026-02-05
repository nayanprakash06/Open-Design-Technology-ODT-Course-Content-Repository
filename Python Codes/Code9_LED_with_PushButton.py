# Import the Pin class to control ESP32 GPIO pins
from machine import Pin

# Import time module to introduce delays
import time

# Create a Pin object for the push button
# GPIO pin 32 is configured as an INPUT pin
# Internal PULL_UP resistor is enabled
# Button NOT pressed → value = 1
# Button pressed     → value = 0
my_Push_Button = Pin(32, Pin.IN, Pin.PULL_UP)

# Create a Pin object for the LED
# GPIO pin 22 is configured as an OUTPUT pin
my_led = Pin(22, Pin.OUT)

# Start an infinite loop
# The program continuously checks the button state
while True:

    # Read the current state of the push button
    Push_Button_values = my_Push_Button.value()

    # Check if the button is pressed
    # Since pull-up is used, pressed condition gives value 0
    if Push_Button_values == 0:

        # Turn the LED ON when the button is pressed
        my_led.on()

        # Print message indicating button press
        print("Button Pressed")

    else:
        # Turn the LED OFF when the button is released
        my_led.off()

    # Wait for 0.2 seconds before checking the button again
    time.sleep(0.2)
