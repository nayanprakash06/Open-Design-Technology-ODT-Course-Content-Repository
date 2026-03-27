from machine import Pin
import time

sensor = Pin(27,Pin.IN) #Sensor Connected to Pin27

#Initialization Time of 60 seconds
print("Sensor Initialization")
for i in range(60):
    print("Time elapsed:",i,"s")
    time.sleep(1)
print("Sensing Now..")

while True :
    
    if sensor.value() == 1 :
        print("Motion Detected")
        
    time.sleep(1)
