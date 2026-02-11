from machine import Pin #Importing Machine module 
import time #Importing time module
import neopixel

pb1 = Pin(4,Pin.IN,Pin.PULL_UP) #Object for Push Button 1
pb2 = Pin(5,Pin.IN,Pin.PULL_UP) #Object for Push Button 2
np = neopixel.NeoPixel(Pin(14),16) #Object for Neopixel

my_count = 0

while True: #Infinte Loop to continously run the loop
    val1 = pb1.value()#Reading value of Push Button1
    val2 = pb2.value()#Reading value of Push Button2
    
    if val1 == 0 and val2 == 0:#Checking of both buttons are pressed.This condition gets priority
        for i in range(0,16,1):#Resetting all leds to off
            np[i] = (0,0,0)
        np.write()
        my_count = 0
        
    elif val1 == 0 and val2 == 1:#Checking if only Button 1 is pressed
        if my_count < 16:#Only 16 LEDs,above 15 will give index error
            np[my_count] = (255,0,0) #LED ON index is the counter
            np.write()
            my_count = my_count + 1 #Increment Counter
        
    elif val1 == 1 and val2 == 0:#Checking if only Button 2 is pressed
        if my_count > 0:#less than 0 will give index error
            my_count = my_count - 1 #Decrement Counter
            np[my_count] = (0,0,0) #LED OFF index is the counter
            np.write()
    
    time.sleep(0.3)#Delay for system stability



