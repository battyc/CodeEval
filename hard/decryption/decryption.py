'''
program: Decryption
author: Chris Batty

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
'''
 B  H  I  S  O  E  C  R  T  M  G  W  Y  V  A  L  U  Z  D  N  F  J  K  P  Q  X
01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 
 A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
 R  T  M  G  W  Y  V  A  L  U  Z  D  N  F  J  K  P  Q  X  B  H  I  S  O  E  C


A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z
+12 +1 +22  +11 +25 +11 +4  +20 +20 +14 +14 +22 +3  +20





01 22 22 __ 11 14 14 25 03 __ 03 13 01 25 13 __ 03 14 14 18 19 21 02 __ 01 13 __ 24 19 18 21 19 02 17 13 06 13 17 15 07 01 19
B  J  J     G  V  V  Q  I     I  Y  B  Q  Y     I  V  V  Z  D  F  H     B  Y     P  D  Z  F  D  H  U  Y  E  Y  U  A  C  B  D
T  I  I                            E  T     E                             T  E                          E     E           T
'''