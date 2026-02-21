# Multiple Sensor Monitoring
# Sensors:
#   - IR Obstacle Sensor
#   - LDR / Light Sensor Module
#   - Sound Sensor Module
from machine import Pin
import time
# Configure sensor pins as INPUT with internal pull-up
obstacle = Pin(15, Pin.IN, Pin.PULL_UP)
light = Pin(4, Pin.IN, Pin.PULL_UP)
sound = Pin(5, Pin.IN, Pin.PULL_UP)

while True:
    # Read sensor values continously
    obs_val = obstacle.value()
    light_val = light.value()
    sound_val = sound.value()
    # If sensor output goes LOW → detection
    if obs_val == 0:
        print("Obstacle Detected")
        
    if light_val == 0:
        print("Light Detected")
    
    if sound_val == 0:
        print("Sound Detected")
        
    # Small delay to avoid flooding serial monitor and system stability
    time.sleep(0.2)