'''
program: Decryption
author: Chris Batty

**NOTE**

This challenge requires more knowledge of cryptography than I possess, inspiring me to work through the educational crypto problem set
found at cryptopals.com.  Once I complete the progression there I will come back and solve this challenge.

**/NOTE**

Decrypt a message given a keyed alphabet.
'''
import operator

message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119"
keyed_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"

messageArray = message.split(' ')
ansList = {}

for c in messageArray:
	line = list(c)
	for i, char in enumerate(line):
		if (i+2)%2 == 0:
			temp = "".join(line[i:i+2])
			if temp in ansList:
				ansList[temp] += 1
			else:
				ansList[temp] = 1
sortedAns = sorted(ansList.items(), key=operator.itemgetter(1), reverse=True)
for val in sortedAns:
	print(val)