import network
import socket
from machine import Pin

# ---------- LED SETUP ----------
led = Pin(2, Pin.OUT)

# ---------- ACCESS POINT ----------
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32-Control', password='12345678')

print("Connect to WiFi: ESP32-Control")
print("IP Address:", ap.ifconfig()[0])


# ---------- HTML PAGE ----------
def webpage():
    html = """<!DOCTYPE html>
<html>
<head>
    <title>ESP32 LED Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: #0f2027;
            color: white;
            padding: 40px;
        }
        button {
            padding: 15px 30px;
            font-size: 18px;
            margin: 10px;
            border: none;
            border-radius: 10px;
        }
        .on { background: #00c853; color: white; }
        .off { background: #d50000; color: white; }
    </style>
</head>
<body>
    <h1> ESP32 LED Control</h1>
    <p>Control the LED using WiFi</p>
    <a href="/on"><button class="on">ON</button></a>
    <a href="/off"><button class="off">OFF</button></a>
</body>
</html>
"""
    return html


# ---------- SOCKET SERVER ----------
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Server running...")

while True:
    conn, addr = server.accept()
    print("Client connected:", addr)

    request = conn.recv(1024)
    request = str(request)

    # ---------- HANDLE REQUEST ----------
    if '/on' in request:
        print("LED ON")
        led.value(1)

    if '/off' in request:
        print("LED OFF")
        led.value(0)

    # ---------- SEND RESPONSE ----------
    response = webpage()

    conn.send("HTTP/1.1 200 OK\r\n")
    conn.send("Content-Type: text/html\r\n")
    conn.send("Connection: close\r\n\r\n")
    conn.sendall(response)

    conn.close()