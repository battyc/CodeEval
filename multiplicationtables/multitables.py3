'''
program: Multiplication Table
author: Chris Batty
'''
row = 1

while row <= 12:
	col = 1
	while col <= 12:
		print(str(row*col).rjust(4), end="")
		col += 1
	print("")
	row += 1