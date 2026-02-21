# Stepper Motor Control using Wave Drive (Single Coil Mode)
from machine import Pin
import time
# Define GPIO pins connected to the stepper motor driver inputs
in1 = Pin(14, Pin.OUT)
in2 = Pin(27, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(25, Pin.OUT)
# Wave Drive Sequence : Only one coil is energized at a time.
# Each inner list represents:[IN1, IN2, IN3, IN4]
seq = [
    [1, 0, 0, 0],  # Step 1 → Energize Coil A
    [0, 1, 0, 0],  # Step 2 → Energize Coil B
    [0, 0, 1, 0],  # Step 3 → Energize Coil C
    [0, 0, 0, 1]   # Step 4 → Energize Coil D
]

# Delay between each step (in seconds)
# 0.005 sec = 5 ms → controls motor speed
my_delay = 0.005

while True:
    # Rotate Clockwise
    # 2000 iterations ≈ one full rotation (for 28BYJ-48 stepper motor in full-step mode)
    for _ in range(2000):
        for step in seq:
            in1.value(step[0])
            in2.value(step[1])
            in3.value(step[2])
            in4.value(step[3])
            time.sleep(my_delay)
    # Rotate Counter-Clockwise
    # Reversing the sequence reverses direction
    for _ in range(2000):
        for r_step in reversed(seq):
            in1.value(r_step[0])
            in2.value(r_step[1])
            in3.value(r_step[2])
            in4.value(r_step[3])
            time.sleep(my_delay)