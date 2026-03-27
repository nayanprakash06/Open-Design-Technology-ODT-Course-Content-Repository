from machine import Pin
import bluetooth
import time
import random

conn_handle = None
value = ""
name = "ESP32-Nayan" #Name of Your ESP32 (Change it to avoid Confusion)
ble = bluetooth.BLE()

ble.active(False)
time.sleep(0.5)
ble.active(True)
ble.config(gap_name=name)

service_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
char_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

char = (char_UUID, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY)
service = (service_UUID, (char,),)
((char_handle,),) = ble.gatts_register_services((service,))

def event_occured(event, data):
    
    global conn_handle 

    if event == 1:
        conn_handle = data[0]
        print("Connected")
        
    elif event == 2:
        conn_handle = None
        print("Disconnected")
        advertise(name)
                  

def advertise(device_name):
    
    name_bytes = device_name.encode()

    flags = bytearray([0x02, 0x01, 0x06])
    short_name = bytearray([len(name_bytes) + 1, 0x08]) + name_bytes
    full_name = bytearray([len(name_bytes) + 1, 0x09]) + name_bytes
    adv_data = flags + short_name + full_name

    ble.gap_advertise(50, adv_data=adv_data)
    print("Awating Connection...Advertising as:", device_name)

advertise(name)

ble.irq(event_occured)

while True:
    #Generating Sensor values(just as an example) using Random
    sensor_value = random.randint(0, 100)
    print("Generated :", sensor_value)
    
    # Update characteristic value
    ble.gatts_write(char_handle, str(sensor_value))
    
    if conn_handle is not None:
        ble.gatts_notify(conn_handle, char_handle)

    time.sleep(1)

