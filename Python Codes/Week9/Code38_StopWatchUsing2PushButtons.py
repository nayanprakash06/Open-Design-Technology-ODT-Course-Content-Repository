from machine import Pin
import time

Button1 = Pin(22, Pin.IN, Pin.PULL_UP)
Button2 = Pin(23, Pin.IN, Pin.PULL_UP)

t1 = None

while True:
    
    if Button1.value() == 0 and t1 is None:
        t1 = time.ticks_ms()
        print("Timer Started")
        time.sleep(0.2)  # debounce
        
    elif Button2.value() == 0 and t1 is None:
        print("Timer not started")
        time.sleep(0.2)
    
    elif Button2.value() == 0 and t1 is not None:
        t2 = time.ticks_ms()
        print("Timer Stopped")
        t = time.ticks_diff(t2, t1)
        print("Time Elapsed:", t, "milliseconds")
        t1 = None  # reset timer
        time.sleep(0.2)
        
    time.sleep(0.2) #Mandatory for System Stability