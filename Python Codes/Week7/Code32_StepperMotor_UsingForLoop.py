# Stepping Mode: Wave Drive (Single Coil Excitation)
from machine import Pin
import time

in1 = Pin(14,Pin.OUT)
in2 = Pin(27,Pin.OUT)
in3 = Pin(26,Pin.OUT)
in4 = Pin(25,Pin.OUT)
# Wave Drive Sequence : Only one coil is energized at a time.
# Each inner list represents:[IN1, IN2, IN3, IN4]
seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

my_delay = 0.005

while True:
    for step in seq:
        in1.value(step[0])
        in2.value(step[1])
        in3.value(step[2])
        in4.value(step[3])
        time.sleep(my_delay)
        