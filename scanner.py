#!/usr/bin/env python3
import pyfiglet
import socket

#banner
text = pyfiglet.figlet_format("PORT SCANNER")
print(text)

#get data
host = input("Enter the host or IP address : ")
port = int(input("Enter the port : "))

#port scanning
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
result = s.connect_ex((host, port))
data = s.recv(1024).decode()
s.close()

#print results
if result == 0:
	print(f"{port} is open")
else:
	print(f"{port} is closed")
print(f"Received data : {data}")