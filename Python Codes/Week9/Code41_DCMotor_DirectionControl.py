from machine import Pin
import time

IN1 = Pin(22, Pin.OUT)
IN2 = Pin(23, Pin.OUT)

while True:
    # Rotate DC Motor in clockwise direction for 3 seconds
    IN1.value(1) #Same as IN1.on()
    IN2.value(0)
    time.sleep(3)
    
    # Stop briefly before changing direction
    IN1.value(0)
    IN2.value(0)
    time.sleep(0.5)

    # Rotate DC Motor in anti-clockwise direction for 3 seconds
    IN1.value(0)
    IN2.value(1)
    time.sleep(3)

    # Stop rotation for 1 second
    IN1.value(0)
    IN2.value(0)
    time.sleep(0.5)