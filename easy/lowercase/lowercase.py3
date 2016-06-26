'''
program: lowercase
author: Chris Batty

This program takes a text file and converts each line to lower case.
'''

import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

for l in fileList:
	print(l.lower(), end="")