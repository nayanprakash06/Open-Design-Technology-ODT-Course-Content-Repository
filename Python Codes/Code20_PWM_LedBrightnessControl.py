# Import the Pin and PWM classes from the machine module
# Pin is used to control GPIO pins
# PWM is used to generate Pulse Width Modulation signals
from machine import Pin, PWM

# Import time module to use delays (sleep)
import time


# Create a PWM object on GPIO pin 4
# Pin(4, Pin.OUT) sets GPIO 4 as an OUTPUT pin
# PWM(...) enables PWM functionality on that pin
my_pwm_led = PWM(Pin(4, Pin.OUT))


# Set the PWM frequency to 1000 Hz (1 kHz)
# This means the PWM signal completes 1000 ON-OFF cycles every second
# A higher frequency avoids visible flickering in LEDs
my_pwm_led.freq(1000)


# Infinite loop so the LED keeps fading in and out continuously
while True:

    # ---------------- FADE IN ----------------
    # This for-loop increases brightness gradually

    # range(0, 1024, 1) means:
    # start at 0       → LED completely OFF
    # stop at 1024     → loop runs till 1023 (max duty)
    # step by 1        → smooth brightness increase
    for x in range(0, 1024, 1):

        # Set PWM duty cycle to value of x
        # duty controls how long the signal stays ON in each cycle
        # 0     → 0% duty cycle  → LED OFF
        # 1023  → ~100% duty     → LED fully ON
        my_pwm_led.duty(x)

        # Small delay so brightness change is visible to the human eye
        # Without this, the fade would be too fast to notice
        time.sleep(0.01)


    # ---------------- FADE OUT ----------------
    # This for-loop decreases brightness gradually

    # range(1023, -1, -1) means:
    # start at 1023    → LED fully ON
    # stop at -1       → loop stops after reaching 0
    # step by -1       → counting backwards
    for y in range(1023, -1, -1):

        # Set PWM duty cycle to value of y
        # As y decreases, ON-time reduces, making LED dimmer
        my_pwm_led.duty(y)

        # Small delay for smooth fading effect
        time.sleep(0.01)
