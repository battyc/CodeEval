'''
program: File Size
author: Chris Batty

Checks the size of a given file
'''
import sys
import os
print(os.path.getsize(sys.argv[1]))