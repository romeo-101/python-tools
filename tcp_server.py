#!/usr/bin/env python3
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 4444))
s.listen(5)
print("[+] Server is listening in port 4444 ....")
conn, addr = s.accept()
print(f"[+] Server is connected to : {addr} ....")
conn.send(b"Hello client!!! this is server")
data = conn.recv(1024).decode()
print(f"Received message : {data} ")
print(f"Client details : {conn}")
conn.close() 