# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 23:14:51 2021

@author: DBarros
"""

import urllib
import bs4
import json

#https://www.py4e.com/code3/json2.py?PHPSESSID=cab1f3fc4a1bb5a9ba20a20af3042593
url="http://py4e-data.dr-chuck.net/comments_1339008.json"
#url = input("Enter the url: ")
handler = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(handler,"html.parser")
info = json.loads(soup.text)

count=0
print('User count:', len(info["comments"]))
for item in info["comments"]:
    print('Name', item['name'])
    print('count', item['count'])
    count+=item["count"]
    print('Count is now: %d' % count)