# Ultrasonic Distance Measurement using HC-SR04 using time_pulse_us()
from machine import Pin, time_pulse_us
import time
# Define Trigger and Echo pins
trig = Pin(27, Pin.OUT)
echo = Pin(14, Pin.IN)

while True:
    # STEP 1: Send 10 µs Trigger Pulse
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    # STEP 2: Measure HIGH pulse duration on Echo pin
    # time_pulse_us(pin, pulse_level, timeout)
    # pin         → echo pin
    # pulse_level → 1 (measure HIGH pulse)
    # timeout     → maximum wait time in microseconds
    # Returns:
    #   Pulse duration in microseconds
    #   -1 if timeout waiting for pulse to start
    #   -2 if timeout waiting for pulse to end
    duration = time_pulse_us(echo, 1, 30000)  # 30 ms timeout
    # STEP 3: Check for Timeout Errors
    if duration < 0:
        print("No object detected (Timeout)")
    else:
        # STEP 4: Convert Duration to Distance (cm)
        # distance(cm) = duration / 58
        # Derived from:
        # Distance = (Speed of Sound × Time) / 2
        distance = duration / 58
        print("Distance:", distance, "cm")

    time.sleep(1)