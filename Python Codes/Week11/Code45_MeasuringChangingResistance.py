from machine import Pin, ADC
import time

bend_sensor = ADC(Pin(34))

bend_sensor.atten(ADC.ATTN_11DB)

while True:
    sensor_val = bend_sensor.read()
    print(sensor_val)
    time.sleep(0.5)
    