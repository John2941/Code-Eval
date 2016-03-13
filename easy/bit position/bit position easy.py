"""
@Project Name - bit position easy
@author - Johnathan
@date - 2/7/2016
@time - 4:43 PM

Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1 and p2 are 1 based.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated list of 3 integers, one list per line. E.g.



86,2,3
125,1,2
OUTPUT SAMPLE:

Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase). E.g.


true
false


"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		number, first_el, second_el = x.strip('\n').split(',')
		binary = bin(int(number))
		if binary[int(first_el)] == binary[int(second_el)]:
			sys.stdout.write( 'true\n' )
		else:
			sys.stdout.write( 'false\n' )