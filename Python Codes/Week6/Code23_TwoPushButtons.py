from machine import Pin #Importing Machine module 
import time #Importing time module

pb1 = Pin(4,Pin.IN,Pin.PULL_UP) #Object for Push Button 1
pb2 = Pin(5,Pin.IN,Pin.PULL_UP) #Object for Push Button 2

while True: #Infinte Loop to continously run the loop
    val1 = pb1.value()#Reading value of Push Button1
    val2 = pb2.value()#Reading value of Push Button2
    
    if val1 == 0:#Checking if Button 1 is pressed
        print("only Button1 Pressed")
        
    if val2 == 0:#Checking if Button 2 is pressed
        print("only Button2 Pressed")
    
    time.sleep(0.2)#Delay for system stability