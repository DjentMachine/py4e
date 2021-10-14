# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:46:43 2021

Python for everybody: Assignement ?
~Finding the numbers in a haysack~

@author: DBarros
"""

import re
import os

os.chdir(****)
#os.getcwd()

file=open("regex_sum_1339003.txt")

numbers=re.findall("[0-9]+",file.read())
numbers=[int(i) for i in numbers]
print(sum(numbers))