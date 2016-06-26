'''
program: String Permutations
author: Chris Batty

this program accepts a file with one string per line and outputs all possible permutations of that string sorted 
and separated by commas.

Sorting assumes that we digits > upper case > lower case moving from left to right. (i.e. Zu6 sorts to 6Zu)
'''

def perms(pre, line):
	if len(line) == 1:
		finalList.append(pre + "".join(line))
	else:
		for i in range(0,len(line)):
			temp = copy.copy(line)
			del(temp[i])
			perms(pre + str(line[i]), temp)
	return

import sys
import copy

f = open(sys.argv[1], "r")
fileList = f.readlines()

for l in fileList:
	passLine = list(sorted(l.replace('\n', ''), key= lambda char: char))
	finalList = []
	perms("", passLine)
	print(",".join(finalList))