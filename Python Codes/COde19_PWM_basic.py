# Import Pin and PWM classes
from machine import Pin, PWM

# Create a Pin object on GPIO 4 as output
my_led_pin = Pin(4, Pin.OUT)

# Create PWM object using the pin
my_pwm_led = PWM(my_led_pin)

# Set PWM frequency to 1000 Hz (1 kHz)
my_pwm_led.freq(1000)

# Set duty cycle
# Range: 0–1023 (0 = OFF, 1023 = full brightness)
my_pwm_led.duty(512)   # ~50% brightness
