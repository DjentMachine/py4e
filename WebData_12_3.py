# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 23:14:51 2021

@author: DBarros
"""

import urllib
import bs4
import re

#"http://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = input("Enter the url: ")
position=int(input("Enter position to search: "))
iterations=int(input("Enter iterations nr: "))
handler = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(handler,"html.parser")
tags= soup("a")

for i in range(iterations):
    url = tags[position-1].get("href", None)    
    handler = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(handler,"html.parser")
    tags= soup("a")
    print(url)

print(re.findall("([A-Z].+)\.",url))