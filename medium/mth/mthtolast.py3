'''
program: mthToLast
author: Chris Batty
'''
import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()
for i in fileList:
	splitList = i.replace('\n', '').split(' ')
	m = int(splitList[-1])
	del splitList[-1]
	length = len(splitList)
	if length >= m:
		print (splitList[length-m])