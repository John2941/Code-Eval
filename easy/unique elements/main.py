"""
@Project Name - unique elements easy
@author - Johnathan
@date - 2/7/2016
@time - 4:40 PM

INPUT SAMPLE:

File containing a list of sorted integers, comma delimited, one per line. E.g.

1
2
1,1,1,2,2,3,3,4,4
2,3,4,5,5

OUTPUT SAMPLE:

Print out the sorted list with duplicates removed, one per line.
E.g.

1
2
1,2,3,4
2,3,4,5
"""
import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		print ','.join(set(x.strip('\n').split(',')))