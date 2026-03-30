import network
import socket

# ---------- ACCESS POINT SETUP ----------
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32-ODT', password='12345678')  # min 8 chars

print("Access Point Active")
print("Connect to WiFi: ESP32-WiFi")
print("IP Address:", ap.ifconfig()[0])

# ---------- SOCKET SERVER ----------
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket()
server.bind(addr)
server.listen(1)

print("Web server running...")

# ---------- HTML PAGE ----------
html = """<!DOCTYPE html>
<html>
<head>
    <title>ODT WiFi Lab</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: white;
            text-align: center;
            padding: 50px;
        }
        .card {
            background: rgba(0,0,0,0.2);
            padding: 30px;
            border-radius: 15px;
            display: inline-block;
        }
        h1 {
            margin-bottom: 10px;
        }
        p {
            font-size: 18px;
        }
        .tag {
            margin-top: 20px;
            font-size: 14px;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>  Welcome to ODT!</h1>
        <p>Today you will be learning the basics of using WiFi with ESP32.</p>
        <p>You've successfully connected to your own microcontroller-powered network  </p>
        <div class="tag">Built using ESP32 + MicroPython</div>
    </div>
</body>
</html>
"""

while True:
    conn, addr = server.accept()
    print("Client connected from", addr)

    request = conn.recv(1024)  # receive request (not used here)

    conn.send("HTTP/1.1 200 OK\r\n")
    conn.send("Content-Type: text/html\r\n")
    conn.send("Connection: close\r\n\r\n")
    conn.sendall(html)

    conn.close()
