#!/usr/bin/env python3
#import module

from bs4 import BeautifulSoup as BS
#open the file and get its content

with open("index.html", "r") as file:
	html_content = file.read()

#create an obj
obj = BS(html_content, "html.parser")

#print the title
print(obj.title.text)

#print the h1 tag's text
print(obj.h1.text)

#find all links
for link in obj.find_all('a'):
	print(link["href"])

#print the all visible text
print(obj.get_text())

#modify the element's content
tag = obj.h1
tag.string = "Dummy text was modified"
print(obj.get_text())