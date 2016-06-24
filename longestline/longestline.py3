'''
program: Longest Lines
author: Chris Batty

Checks the first line of an input file for a number n and then prints the n longest lines
in the file.
'''
import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

numLongest = int(fileList[0])
del(fileList[0])

fileList.sort(key = len, reverse=True)

for index in range(0, numLongest):
	print(fileList[index], end="")