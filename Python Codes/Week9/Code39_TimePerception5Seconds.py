from machine import Pin
import time

Button1 = Pin(22, Pin.IN, Pin.PULL_UP)
Button2 = Pin(23, Pin.IN, Pin.PULL_UP)

t1 = None

while True:
    
    if Button1.value() == 0 and t1 is None:
        t1 = time.ticks_ms()
        print("Timer Started")
        
    elif Button2.value() == 0 and t1 is None:
        print("Timer not started")
    
    elif Button2.value() == 0 and t1 is not None:
        t2 = time.ticks_ms()
        print("Timer Stopped")
        t = time.ticks_diff(t2, t1)
        print("Time Elapsed:", t, "milliseconds")
        print("Difference from 5 seconds:", abs(5 - t / 1000), "seconds")
        t1 = None
    
    time.sleep(0.2)