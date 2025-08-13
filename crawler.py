#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as BS

url = input("Enter the URL : ")
head = {
	"User-Agent":  "Mozilla/5.0 (X11; Linux x86_64)"
}
response = requests.get(url, headers=head)
if response.status_code == 200:
	obj = BS(response.content,"html.parser")
	for link in obj.find_all('a'):
		print(f"link : {link.get('href')}")
else:
	print(f"{response.status_code} ERROR FAILED TO FETCH THE URL {url}")
#https://en.wikipedia.org/wiki/Amazon_(company)