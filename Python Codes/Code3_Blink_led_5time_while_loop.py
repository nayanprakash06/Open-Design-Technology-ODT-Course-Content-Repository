# Import the Pin class to control GPIO pins of the ESP32
from machine import Pin

# Import time module to use delay functions
import time

# Create a Pin object for the LED
# GPIO pin 22 is configured as an OUTPUT pin
my_led = Pin(22, Pin.OUT)

# Initialize a counter variable
# This will keep track of how many times the LED blinks
my_count = 1

# Start a while loop
# The loop will run as long as my_count is less than 6
while (my_count < 6):

    # Turn the LED ON
    my_led.on()

    # Keep the LED ON for 0.5 seconds
    time.sleep(0.5)

    # Turn the LED OFF
    my_led.off()

    # Keep the LED OFF for 0.5 seconds
    time.sleep(0.5)

    # Print the current blink number on the serial console
    print("Blink Number:", my_count)

    # Increment the counter by 1
    # This ensures the loop eventually stops
    my_count = my_count + 1

# This statement executes after the while loop finishes
# It indicates that the program has completed its execution
print("Execution Complete")
