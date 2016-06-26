'''
program: cycledetection
author: Chris Batty
'''
def findCycle(line):
	numList = line.replace('\n', '').split(' ')
	listCount = len(numList)
	startPointer =  numList[0]
	startPointerIndex = 0
	compareIndex = 1
	cycleFound = False
	noCycle = False
	while cycleFound != True and noCycle != True:
		while compareIndex < listCount:
			if startPointer == numList[compareIndex]:
				if compareIndex - startPointerIndex == 1:
					return [startPointer]
				else:
					cycleLen = compareIndex - startPointerIndex
					if compareIndex + cycleLen <= listCount - 1:
						cycleMatch = True
						for num in range(0,cycleLen-1):
							if numList[startPointerIndex + num] != numList[compareIndex + num]:
								cycleMatch = False
								break
						if cycleMatch == True:
							return numList[startPointerIndex:compareIndex]

			compareIndex += 1
		startPointerIndex+=1
		if startPointerIndex == listCount - 1:
			return "None"
		startPointer = numList[startPointerIndex]
		compareIndex = startPointerIndex+1

import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()
for line in fileList:
	ans = findCycle(line)
	for num in ans:
		print(num, end=" ")
	print("")



