'''
program: sum of digits
author: Chris Batty

This program takes a text file of integers and calculates the sum of each character in the number.  i.e. if the text file has the number 23, the program outputs 5
'''

import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

for l in fileList:
	sum = 0
	for num in list(map(int,l.replace('\n', ""))):
		sum += num
	print(sum)