from machine import Pin
import bluetooth
import time

ble = bluetooth.BLE()
ble.active(True)

# UUIDs
SERVICE_UUID = bluetooth.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
CHAR_UUID = bluetooth.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

# Characteristic only needs WRITE
CHAR = (CHAR_UUID, bluetooth.FLAG_WRITE)

SERVICE = (SERVICE_UUID, (CHAR,),)

((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

def irq(event, data):
    
    global connections
    # Event 1 → Phone Connected
    if event == 1:
        conn_handle, addr_type, addr = data
        connections.add(conn_handle)
        print("Phone connected")
    
    # Event 2 → Phone Disconnected
    elif event == 2:
        conn_handle, addr_type, addr = data
        connections.remove(conn_handle)
        print("Phone disconnected")
        advertise()
        
    # Event 3 → phone wrote data
    elif event == 3:
        conn_handle, value_handle = data

        if value_handle == char_handle:

            msg = ble.gatts_read(char_handle).decode().strip()

            print("Received from phone:", msg)
            

ble.irq(irq)


def advertise():
    name = "ESP32-ESP1"

    adv_data = bytearray()
    adv_data += bytearray((len(name) + 1, 0x09)) + name.encode()

    ble.gap_advertise(100, adv_data)

    print("Advertising as:", name)


advertise()

print("Waiting for phone connection...")

while True:
    time.sleep(1)
