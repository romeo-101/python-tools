#!/usr/bin/env python3
import json
with open("info.json", "r") as f:
	json_string = json.load(f)
	print("Password is ",json_string["credentials"]["password"])
	