#!/usr/bin/env python3
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect(("127.0.0.1", 4444))
data = s.recv(1024).decode()
print(f"Received message : {data}")
s.send(b"Hello Server! this is client")
print(f"Result : {res}")
s.close()