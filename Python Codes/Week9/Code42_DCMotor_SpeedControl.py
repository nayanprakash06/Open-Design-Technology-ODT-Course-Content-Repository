from machine import Pin,PWM
import time

IN1 = Pin(22, Pin.OUT)
IN2 = Pin(23, Pin.OUT)
en = PWM(Pin(15),freq=1000)

while True:
    # Rotate DC Motor in clockwise direction for 3 seconds with Speed 1 (Lower Speed/RPM)
    en.duty(700)
    IN1.value(1) 
    IN2.value(0)
    time.sleep(3)
    
    # Stop briefly for 0.5s
    IN1.value(0)
    IN2.value(0)
    time.sleep(0.5)
    
    # Rotate DC Motor in clockwise direction for 3 seconds with Speed 2 (Medium Speed/RPM)
    en.duty(850)
    IN1.value(1) 
    IN2.value(0)
    time.sleep(3)
    
    # Stop briefly for 0.5s
    IN1.value(0)
    IN2.value(0)
    time.sleep(0.5)
    
    # Rotate DC Motor in clockwise direction for 3 seconds with Speed 3 (Max Speed/RPM)
    en.duty(1023)
    IN1.value(1) 
    IN2.value(0)
    time.sleep(3)
    
    # Stop briefly for 0.5s
    IN1.value(0)
    IN2.value(0)
    time.sleep(0.5)
