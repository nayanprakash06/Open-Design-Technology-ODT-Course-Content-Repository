from machine import Pin
import bluetooth
import time

led1 = Pin(22,Pin.OUT)
led2 = Pin(23,Pin.OUT)

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

def my_led_pattern1():
    led1.off()
    led1.on()
    led2.off()
    time.sleep(1)
    led1.off()
    led2.on()
    time.sleep(1)
    
def my_led_pattern2():
    led1.on()
    led2.on()
    time.sleep(1)
    led1.off()
    led2.off()
    time.sleep(1)


while True:

    if value == "1":
        print("Loop 1")
        my_led_pattern1()
        value = ""
    elif value == "2":
        print("Loop 2")
        my_led_pattern2()
        value = ""
    
    time.sleep(0.2)

