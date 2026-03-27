from machine import Pin
import time

led1 = Pin(22,Pin.OUT)
led2 = Pin(23,Pin.OUT)
led3 = Pin(14,Pin.OUT)
led4 = Pin(15,Pin.OUT)

def my_blynk(num_of_blink,speed):
    for _ in range(num_of_blink):
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        time.sleep(speed)
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(speed)

def only_on(duration):
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    time.sleep(duration)
      
def mg_hector(speed_of_motion):
    led1.on()
    time.sleep(speed_of_motion)
    led1.off()
    led2.on()
    time.sleep(speed_of_motion)
    led2.off()
    led3.on()
    time.sleep(speed_of_motion)
    led3.off()
    led4.on()
    time.sleep(speed_of_motion)
    led4.off()
    
def all_off():
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    time.sleep(0.1)
    
while True :
    all_off()
    my_blynk(2,0.5)
    all_off()
    only_on(2)
    all_off()
    mg_hector(0.3)
    all_off()
    my_blynk(3,1)
    
    