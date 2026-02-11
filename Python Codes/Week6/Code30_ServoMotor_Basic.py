from machine import Pin,PWM
#DutyCycle of PWM corresponds to position of the...
#...shaft of the servomotor
import time#For delay

my_servo = PWM(Pin(4),freq=50)#Always keep frequency Constant @ 50Hz

while True:#Continous running of the loop
    my_servo.duty(35)#Move the shaft to approx. 0 degree
    time.sleep(2)#Give it some time to reach the position
    my_servo.duty(110)#Move the shaft to approx. 180 degree
    time.sleep(2)#Give it some time to reach the position