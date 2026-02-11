# Import the Pin class from the machine module
# Pin is used to configure and control ESP32 GPIO pins
from machine import Pin

# Import time module to introduce delays in the program
import time


# Create a Pin object for the IR obstacle sensor
# GPIO 22 is connected to the digital output of the IR sensor
# Pin.IN configures the pin as an input
# Pin.PULL_UP enables the internal pull-up resistor
# This keeps the pin HIGH (1) when no obstacle is detected
my_ir_sensor = Pin(22, Pin.IN, Pin.PULL_UP)


# Create a Pin object for the LED
# GPIO 23 is connected to the LED
# Pin.OUT configures the pin as an output so we can turn it ON or OFF
my_led = Pin(23, Pin.OUT)


# Infinite loop so the ESP32 continuously monitors the IR sensor
while True:

    # Read the current digital value from the IR sensor
    # value() returns:
    # 0 → Obstacle detected (sensor pulls the line LOW)
    # 1 → No obstacle detected (pull-up keeps it HIGH)
    ir_values = my_ir_sensor.value()

    # Check if the sensor output is LOW (active-LOW logic)
    if ir_values == 0:

        # Turn ON the LED to indicate obstacle detection
        my_led.on()

        # Print a message to the serial monitor for debugging/feedback
        print("Obstacle Detected")

    else:
        # Turn OFF the LED when no obstacle is detected
        my_led.off()

    # Delay of 0.2 seconds (200 ms)
    # Prevents rapid switching and excessive serial prints
    time.sleep(0.2)
