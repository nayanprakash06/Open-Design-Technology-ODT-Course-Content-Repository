import bluetooth
import random
import time
from micropython import const

# BLE event constants
_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)

# Create BLE object
ble = bluetooth.BLE()
ble.active(True)

# UUIDs for the service and characteristic
SERVICE_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")
CHAR_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")

# Characteristic properties: Notify + Read
CHARACTERISTIC = (
    CHAR_UUID,
    bluetooth.FLAG_NOTIFY | bluetooth.FLAG_READ,
)

# Create service
SERVICE = (
    SERVICE_UUID,
    (CHARACTERISTIC,),
)

# Register service
((char_handle,),) = ble.gatts_register_services((SERVICE,))

connections = set()

# BLE interrupt handler
def ble_irq(event, data):
    global connections
    
    if event == _IRQ_CENTRAL_CONNECT:
        conn_handle, addr_type, addr = data
        print("Phone connected")
        connections.add(conn_handle)

    elif event == _IRQ_CENTRAL_DISCONNECT:
        conn_handle, addr_type, addr = data
        print("Phone disconnected")
        connections.remove(conn_handle)
        advertise()  # restart advertising

ble.irq(ble_irq)

# Advertising function
def advertise():
    name = "ESP32-Sensor"
    adv_data = bytearray('\x02\x01\x06', 'utf-8') + bytearray((len(name) + 1, 0x09)) + name.encode()
    #ble.config(gap_name="ESP32-ODT")
    ble.gap_advertise(100)
    print("Advertising started")

advertise()

# Main loop
while True:

    if connections:
        sensor_value = random.randint(0, 100)
        print("Sending:", sensor_value)

        # Convert to bytes
        data = str(sensor_value)

        # Update characteristic value
        ble.gatts_write(char_handle, data)

        # Notify connected phone
        for conn_handle in connections:
            ble.gatts_notify(conn_handle, char_handle)

    time.sleep(2)