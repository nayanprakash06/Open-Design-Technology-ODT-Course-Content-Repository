# Import the Pin class from the machine module
# Pin is used to configure and control ESP32 GPIO pins
from machine import Pin

# Import time module to add delays in the program
import time


# Create a Pin object for the IR sensor
# Pin number 23 is used for the sensor output
# Pin.IN sets the pin as INPUT (we are reading data from the sensor)
# Pin.PULL_UP enables the internal pull-up resistor
# This keeps the pin at logic HIGH (1) when the sensor is not active
my_ir_sensor = Pin(23, Pin.IN, Pin.PULL_UP)


# Infinite loop so the ESP32 keeps checking the sensor continuously
while True:

    # Read the digital value from the IR sensor
    # value() returns:
    # 1 → No obstacle detected (due to pull-up)
    # 0 → Obstacle detected (sensor pulls the line LOW)
    ir_values = my_ir_sensor.value()

    # Print the sensor value to the serial monitor
    # Useful for debugging and understanding sensor behavior
    print(ir_values)

    # Delay of 0.2 seconds (200 milliseconds)
    # Prevents flooding the serial monitor with too many values
    # Also makes changes easier to observe
    time.sleep(0.2)
