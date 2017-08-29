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

list_of_functions = []

with open('test_fun.txt', 'r') as f1:
	for line in f1:
		line = str(line)
		if "def" in line:
			list_of_functions.append(line.split("def"))

print(list_of_functions)
