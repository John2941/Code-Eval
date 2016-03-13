"""
@Project Name - Mth to the last element moderate
@author - Johnathan
@date - 2/7/2016
@time - 4:53 PM
Write a program which determines the Mth to the last element in a list.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the series of space delimited characters followed by an integer. The integer represents an index in the list (1-based), one per line.

For example:


a b c d 4
e f g h 2
OUTPUT SAMPLE:

Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the number of elements in the list, ignore that input.

For example:

a
g
"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		temp = x.strip('\n').split(' ')
		mth = int(temp[-1])
		temp = temp[:-1]
		if mth > len(temp):
			continue
		sys.stdout.write(temp[mth * -1] + '\n')