'''
program: sum of digits
author: Chris Batty

This program takes a text file of integers and calculates the sum of each character in the number.  i.e. if the text file has the number 23, the program outputs 5
'''

import sys

fpointer = open(sys.argv[1], "r")
file_list = fpointer.readlines()

for line in file_list:
	digit_sum = 0
	for num in list(map(int,line.replace('\n', ""))):
		digit_sum += num
	print(digit_sum)