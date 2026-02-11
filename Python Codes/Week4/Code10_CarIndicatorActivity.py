# Import the Pin class to control ESP32 GPIO pins
from machine import Pin

# Import time module to introduce delays
import time 

# Configure push button 1 as an input with internal pull-up resistor
# GPIO 26 is used
# Not pressed → value = 1, Pressed → value = 0
pb1 = Pin(26, Pin.IN, Pin.PULL_UP)

# Configure push button 2 as an input with internal pull-up resistor
# GPIO 32 is used
# Not pressed → value = 1, Pressed → value = 0
pb2 = Pin(32, Pin.IN, Pin.PULL_UP)

# Configure four LEDs as output pins
# These LEDs will be used to show direction indication
led1 = Pin(4, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(22, Pin.OUT)
led4 = Pin(23, Pin.OUT)

# Start an infinite loop
# The program continuously checks the push buttons
while True :
    
    # Read the current state of push button 1
    pb1_v = pb1.value()

    # Read the current state of push button 2
    pb2_v = pb2.value()

    # Check if push button 1 is pressed
    # This corresponds to a "Turn Right" indication
    if pb1_v == 0 :
        print("Turn Right")

        # Turn OFF all LEDs before starting the sequence
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(0.2)

        # Turn ON LEDs one by one from left to right
        led1.on()
        time.sleep(0.2)
        led2.on()
        time.sleep(0.2)
        led3.on()
        time.sleep(0.2)
        led4.on()
        time.sleep(0.2)
    
    # Check if push button 2 is pressed
    # This corresponds to a "Turn Left" indication
    if pb2_v == 0 :
        print("Turn Left")

        # Turn OFF all LEDs before starting the sequence
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(0.2)

        # Turn ON LEDs one by one from right to left
        led4.on()
        time.sleep(0.2)
        led3.on()
        time.sleep(0.2)
        led2.on()
        time.sleep(0.2)
        led1.on()
        time.sleep(0.2)
    
    # Turn ON all LEDs when no button is pressed
    # This can represent an idle or default state
    led1.on()
    led2.on()
    led3.on()
    led4.on()

    # Small delay to reduce rapid polling
    time.sleep(0.1)
