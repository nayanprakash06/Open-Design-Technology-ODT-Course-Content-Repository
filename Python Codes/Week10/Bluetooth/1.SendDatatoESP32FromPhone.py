from machine import Pin
import bluetooth
import time

name = "ESP32-Nayan" #Name of Your ESP32 (Change it to avoid Confusion)

ble = bluetooth.BLE()
ble.active(False)
time.sleep(0.5)
ble.active(True)
ble.config(gap_name=name)

SERVICE_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
CHAR_UUID    = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

CHAR    = (CHAR_UUID, bluetooth.FLAG_WRITE)
SERVICE = (SERVICE_UUID, (CHAR,),)
((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

def irq(event, data):
    global connections
    if event == 1:
        conn_handle, addr_type, addr = data
        connections.add(conn_handle)
        print("Connected")
        
    elif event == 2:
        conn_handle, addr_type, addr = data
        connections.discard(conn_handle)
        print("Disconnected")
        advertise(name)
        
    elif event == 3:
        conn_handle, value_handle = data
        if value_handle == char_handle:
            msg = ble.gatts_read(char_handle).decode().strip() #Value Received From Phone
            print("Received:", msg)
            
ble.irq(irq)

def advertise(l_name):
    
    name_bytes = l_name.encode()

    flags = bytearray([0x02, 0x01, 0x06])
    short_name  = bytearray([len(name_bytes) + 1, 0x08]) + name_bytes
    full_name   = bytearray([len(name_bytes) + 1, 0x09]) + name_bytes
    adv_data = flags + short_name + full_name

    ble.gap_advertise(50, adv_data=adv_data)
    print("Advertising as:", l_name)

advertise(name)
print("Waiting for connection...")

while True:
    time.sleep(1)