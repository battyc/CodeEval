'''
program: Clean up the words
author: Chris Batty

Print the words from the input file in lower case separated by spaces.  Remove any non-alphabetic characters.
'''
import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

for line in fileList:
	charArray = list(line)
	for i,char in enumerate(charArray):
		if not char.isalpha() == True:
			charArray[i] = ' '
	print((" ".join("".join(charArray).split())).lower())