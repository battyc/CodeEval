'''
program: Trick or Treat
author: Chris Batty

Count all candies.
'''

import sys

# Main Driver #

f = open(sys.argv[1], "r")
fileList = f.readlines()

for line in fileList:
	vampires, zombies, witches, houses = line.split(',')
	vampires = int(vampires.split(': ')[1])
	zombies = int(zombies.split(': ')[1])
	witches = int(witches.split(': ')[1])
	houses = int(houses.split(': ')[1])
	print(str((((vampires*3)+(zombies*4)+(witches*5))*houses)//(vampires+zombies+witches)))