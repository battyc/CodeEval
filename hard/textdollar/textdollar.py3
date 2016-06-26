'''
program: Text Dollar
author: Chris Batty

Print out the text dollar amount of a given quantity
'''
import sys

# Set up a few dictionaries # 
onesDict = {
		'0':"",
		'1':"One",
		'2':"Two",
		'3':"Three",
		'4':"Four",
		'5':"Five",
		'6':"Six",
		'7':"Seven",
		'8':"Eight",
		'9':"Nine",
	}

tensDict = {
		'1':"Ten",
		'11':"Eleven",
		'12':"Twelve",
		'13':"Thirteen",
		'14':"Fourteen",
		'15':"Fifteen",
		'16':"Sixteen",
		'17':"Seventeen",
		'18':"Eighteen",
		'19':"Nineteen",
		'2':"Twenty",
		'3':"Thirty",
		'4':"Forty",
		'5':"Fifty",
		'6':"Sixty",
		'7':"Seventy",
		'8':"Eighty",
		'9':"Ninety",
		'0':"",
	}

largeVals = {
		0: "",
		1: "",
		2: "Thousand",
		3: "Million",
	}

# Main Driver #

f = open(sys.argv[1], "r")
fileList = f.readlines()

for line in fileList:
	line = line.replace('\n', "")
	numLen = len(line)
	charList = list(line)
	skipOnes = False
	currentMult = -(-numLen//3)
	for index,val in enumerate(charList):
		# skips a pass if the last char of a group of 3 is 0
		if skipOnes == True:
			skipOnes = False
			pass
		# Handle the 100's places of each group of 3
		elif((numLen-index)%3) == 0:
			if val!='0':
				print(onesDict[val]+"Hundred", end="")
		# Handle the 10's place
		elif((numLen-index)%3) == 2:
			if(val == "1" and charList[index+1]!='0'):
				print(tensDict[str(val+charList[index+1])] + largeVals[currentMult], end ="")
				skipOnes = True
			else:
				print(tensDict[val], end="")
		# Handle the 1's place of each group of 3
		elif((numLen-index)%3 == 1):
			if(currentMult == 2 and charList[index-2:index+1] == ['0','0','0']):
				pass
			else:
				print(onesDict[val]+largeVals[currentMult], end="")
		# This little trick gets the division ceiling without having to import the math package
		currentMult = -(-(numLen - index)//3)
	print("Dollars")