# -*- coding: utf-8 -*-

"""
Created on Wed Jun 26 13:18:20 2017
@author: Elpida Bantra
"""
import sys
import pygit2
import re
import string
import subprocess
import os
import math


""" this code can be used for text analysis"""


imported_items=[]
document_text = open('testfile.txt', 'r')
text_string = str(document_text.read().lower())
words = text_string.split()
for i,w in enumerate(words):
    if w == "import":
        imported_items.append(words[i+1])

print(imported_items)
        



