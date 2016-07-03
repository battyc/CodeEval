'''
program: Data Recovery
author: Chris Batty

Unscrambles a sentence based on a given pattern.
'''
import sys

fpointer = open(sys.argv[1], "r")
file_list = fpointer.readlines()

for line in file_list:
	words, keys = line.replace('\n', '').split(';')
	words = words.split(" ")
	keys = keys.split(" ")

	output = ["" for i in range(0, len(keys)+1)]

	for index, word in enumerate(words):
		if len(keys) > index:
			output[(int(keys[index])-1)] = words[index]
		else:
			for ind, entry in enumerate(output):
				if entry == "":
					output[ind] = word

	print(" ".join(output))