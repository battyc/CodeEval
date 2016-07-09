'''
program: Decryption
author: Chris Batty

Decrypt a message given a keyed alphabet.

'''

import string

standard_alphabet = list(string.ascii_uppercase)
keyed_alphabet = list("BHISOECRTMGWYVALUZDNFJKPQX")

message_array = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119".split(' ')

message_chars = [[] for num_block in message_array]

for index, block in enumerate(message_array):
	for ind, char in enumerate(list(block)):
		if(ind+2)%2 == 0:
			# Convert numbers to standard alphabet then transpose using keyed alphabet.
			message_chars[index].append(standard_alphabet[keyed_alphabet.index(standard_alphabet[int(block[ind:ind+2])])])
	message_chars[index] = "".join(message_chars[index]) 
print(" ".join(message_chars))

