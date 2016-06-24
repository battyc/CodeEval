'''
program: First Non-Repeating Character
author: Chris Batty

Takes in a file comprised of a string per line.  Outputs the first non-repeating character
from that string to stdout.
'''
import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

for line in fileList:
	charList = list(line.replace('\n',''))
	pointer = 0
	index = 0
	while index < len(charList):
		if index != pointer and charList[pointer] == charList[index]:
			pointer += 1
			index = 0
		else:
			index += 1
	print(charList[pointer])