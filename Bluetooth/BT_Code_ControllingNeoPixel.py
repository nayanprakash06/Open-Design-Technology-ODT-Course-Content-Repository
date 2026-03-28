from machine import Pin
import bluetooth
import time
import neopixel
import random

my_neo = neopixel.NeoPixel(Pin(22), 16)
value = ""
name = "ESP32-Nayan" #Name of Your ESP32 (Change it to avoid Confusion)
ble = bluetooth.BLE()

ble.active(False)
time.sleep(0.5)
ble.active(True)
ble.config(gap_name=name)

service_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
char_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

char = (char_UUID, bluetooth.FLAG_WRITE)
service = (service_UUID, (char,),)
((char_handle,),) = ble.gatts_register_services((service,))

def event_occured(event, data):

    if event == 1:
        print("Connected")
        
    elif event == 2:
        print("Disconnected")
        advertise(name)
        
    elif event == 3:
        conn_handle, value_handle = data
        if value_handle == char_handle:
        #reading the Value written on characteristics by Phone/client
            raw_msg = ble.gatts_read(char_handle).rstrip(b'\x00')
            msg = raw_msg.decode().strip()
            print("Received:", msg)
                
            global value
            value = msg           

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

def my_neo_star():
    for n in range(0,16):
        my_neo[n] = (0,0,150)
    my_neo.write()
    
def my_neo_bling():
    for k in range(0,16):
        r = random.randint(100,150)
        g = random.randint(100,150)
        b = random.randint(100,150)
        my_neo[k] = (r,g,b)
        time.sleep(0.1)
        my_neo.write()



while True:

    if value == "1":
        print("NeoPixel_Star")
        my_neo_star()
        value = ""
    elif value == "2":
        print("NeoPixel_Bling")
        my_neo_bling()
        value = ""
    
    time.sleep(0.2)

