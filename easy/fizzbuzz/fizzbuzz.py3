'''
program: Fizz Buzz
author: Chris Batty
'''
import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

for i in fileList:
	lineInfo = i.replace('\n', '').split(' ')
	count = 1
	while count <= int(lineInfo[2]):
		if count % int(lineInfo[0]) == 0 and count % int(lineInfo[1]) == 0:
			print("FB", end=" ")
		elif count % int(lineInfo[0]) == 0:
			print("F", end=" ")
		elif count % int(lineInfo[1]) == 0:
			print("B", end=" ")
		else:
			print(count, end=" ")
		count+=1
	print("")