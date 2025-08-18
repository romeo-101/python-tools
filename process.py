#!/usr/bin/env python3
import subprocess as sp
result=sp.run(["echo 'Hello World'"], capture_output=True, text=True, shell=True)
print(result.stdout)
print(result.returncode)