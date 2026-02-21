# Stepping Mode: Wave Drive (Single Coil Excitation)
from machine import Pin
import time

in1 = Pin(14,Pin.OUT)
in2 = Pin(27,Pin.OUT)
in3 = Pin(26,Pin.OUT)
in4 = Pin(25,Pin.OUT)

my_delay = 0.005 # 5 mili seconds delay after each coil exitation 
#200 steps in 1 second

while True:
    #Step 1 (1,0,0,0)
    in1.value(1)#Energising Coil A
    in2.value(0)
    in3.value(0)
    in4.value(0)
    time.sleep(my_delay)#Optimised Delay
    
    #Step 2 (0,1,0,0)
    in1.value(0)
    in2.value(1)#Energising Coil B
    in3.value(0)
    in4.value(0)
    time.sleep(my_delay)
    
    #Step 3 (0,0,1,0)
    in1.value(0)
    in2.value(0)
    in3.value(1)#Energising Coil C
    in4.value(0)
    time.sleep(my_delay)
    
    #Step 4 (0,0,0,1)
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(1)#Energising Coil D
    time.sleep(my_delay)
    
    
    
    


