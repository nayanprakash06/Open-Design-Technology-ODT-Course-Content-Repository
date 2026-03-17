from machine import Pin
import time
import random

led = Pin(2,Pin.OUT)
button = Pin(15,Pin.IN,Pin.PULL_UP)

while True:
    #Idle Stage
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)
    if button.value() == 0 :
        r = random.randint(1000,5000)
        #LED On indicating that Game is Starting
        led.on()
        time.sleep(2)
        led.off()
        time.sleep_ms(r)
        led.on()
        t1 = time.ticks_ms()
        while button.value() == 1 :
            time.sleep_ms(1) #Doing nothing for 1 milli seconds and check button value, just for stability, better than using pass
        t2 = time.ticks_ms()
        #Measuring teh reaction time
        reaction = time.ticks_diff(t2,t1)
        print("Reaction Time:",reaction)
        time.sleep(1)
        
        
        