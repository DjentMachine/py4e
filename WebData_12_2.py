# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:24:02 2021

@author: DBarros
"""

import urllib
import bs4

url = "http://py4e-data.dr-chuck.net/comments_1339005.html"
a = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(a,"html.parser")
tags= soup("span")

tot=0

for tag in tags:
    #print("TAG: ", tag)
    #print("URL: ", tag.get("href", None))
    #print("Contents: ", tag.contents[0])
    #print("Atributes: ", tag.attrs)
    tot+= int(tag.contents[0])
print(tot)