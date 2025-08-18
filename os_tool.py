#!/usr/bin/env python3
import os
out = os.listdir('.')
print("==========Hidden files==========")
j=1
for i in out:
	if i[0] == '.':
		print(f"Hidden file {j} : {i}")
	else:
		continue	
	j+=1
print("==========Directory Enumeration==========")
b=1
for a in out:
	if os.path.isdir(a):
		print(f"Directory {b} : {a}")
	else:
		continue
	b+=1