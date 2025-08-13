#!/usr/bin/env python3
import requests

url = input("Enter the URL : ")
header = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
}
total = int(input("Enter how many directories you want to find : "))

arr = []
with open("/home/osboxes/Downloads/common.txt", "r") as file:
	for line in file:
		a = line.strip()
		arr.append(a)
		if len(arr) < total:
			continue
		else:
			break
for i in arr:
	uri = url + i
	response = requests.get(uri, headers=header, timeout=5)
	if response.status_code == 404:
		continue
	else:
		print(f"url:{uri} status ---> code:{response.status_code}")

print("BRUTE FORCING COMPLETED")

