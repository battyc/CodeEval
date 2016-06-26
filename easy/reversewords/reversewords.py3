'''
program: Reverse Words
author: Chris Batty
'''
import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

for line in fileList:
	wordList = line.replace('\n', '').split(' ')
	wordCount = len(wordList)
	for word in wordList:
		wordCount -= 1
		print(wordList[wordCount], end=" ")
	print("")
