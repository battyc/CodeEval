'''
program: Interrupted Bubble Sort
author: Chris Batty
Sort a list of elements.  Partially.
'''
import sys

# Functions #
def bubbleSortSinglePass(numList, listLen, numPass):
	for i, n in enumerate(numList):
		if(i+1 < listLen-numPass):
			if n > numList[i+1]:
				numList[i], numList[i+1] = numList[i+1], numList[i]
		if(numPass == listLen):
			return True
	return False

# Main Driver #

f = open(sys.argv[1], "r")
fileList = f.readlines()

for line in fileList:
	numList, iterations = line.split(' | ')
	iterations = int(iterations)
	numListPass = [int(num) for num in(numList.split(' '))]
	listLen = len(numListPass)
	solved = False
	for count in range(0, iterations):
		if(solved == False):
			solved = bubbleSortSinglePass(numListPass, listLen, count)
		else:
			break
	print(*numListPass, sep=' ')
