'''
program: ASCII Decryption
author: Chris Batty

'''
# Functions #
def areAlphabet(testArray, offset, leadingSpace):
	shiftedArray = shiftAsciiArray(testArray, offset)
	if leadingSpace == 1:
		if chr(shiftedArray[0]) != ' ':
			return False
		else:
			for asciiVal in shiftedArray[1:]:
				if not chr(int(asciiVal)).isalpha() == True:
					return False
		return True
	else:
		for asciiVal in shiftedArray:
			if not chr(int(asciiVal)).isalpha() == True:
				return False
		return True
		
def getShiftValue(wordLen, lastChar, charArray):
	for index,char in enumerate(charArray):
		if index == 0:
			leadingSpace = 0
		else:
			leadingSpace = 1
		test = (charArray[index:index+wordLen+leadingSpace])
		secondaryArray = list(charArray[index+wordLen+1:])
		for testInd, c in enumerate(secondaryArray):
			secTest = secondaryArray[testInd:testInd+wordLen+leadingSpace]
			if test == secTest:
				offset = ord(lastChar)-int(test[-1])
				#check if all chars are words
				if(areAlphabet(test, offset, leadingSpace) == True):
					return offset
				else:
					pass
	return 0

def shiftAsciiArray(asciiArray, shiftVal):
	respArray = []
	for val in asciiArray:
		intVal = int(val)
		if((intVal + shiftVal) < 0):
			#handle -shiftval that would become negative
			respArray.append((127 + (intVal + shiftVal)))
		elif((intVal + shiftVal) > 127):
			#handle +shiftval that would become positive
			respArray.append((intVal+shiftVal)%127)
		else:
			respArray.append(intVal + shiftVal)
	return respArray

# Main Driver #
import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

for line in fileList:
	lineArray = line.split(' | ')
	shiftVal = getShiftValue(int(lineArray[0]), lineArray[1], lineArray[2].split(' '))
	for entry in shiftAsciiArray(lineArray[2].split(' '), shiftVal):
		print(chr(entry), end="")