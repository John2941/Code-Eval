"""
@Project Name - the major element hard
@author - Johnathan
@date - 3/10/2016
@time - 3:25 PM

THE MAJOR ELEMENT


The major element in a sequence with the length of L is the element which appears in a sequence more than L/2 times. The challenge is to find that element in a sequence.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line of the file contains a sequence of integers N separated by comma. E.g.

92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19
92,11,30,92,1,11,92,38,92,92,43,92,92,51,92,36,97,92,92,92,43,22,84,92,92
4,79,89,98,48,42,39,79,55,70,21,39,98,16,96,2,10,24,14,47,0,50,95,20,95,48,50,12,42

OUTPUT SAMPLE:
For each sequence print out the major element or print "None" in case there is no such element. E.g.

19
92
None
"""

import os
import sys

def count_ocurances(num_list):
	_dict = {}
	for x in set(num_list):
		count = num_list.count(x)
		if count in _dict.keys():
			_dict[count].append(x)
		else:
			_dict[count] = [x]
	return _dict

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	x = input_file.read()
	nums = x.split('\n')
for x in nums:
	if x:
		num_list = x.split(',')
		num_list = map(int, num_list)
		count_dict = count_ocurances(num_list)
		num_list_len = len(num_list)
		answer = ""
		for x in count_dict.keys():
			if x > (num_list_len / 2):
				answer += "".join(str(x) for x in count_dict[x])
				break
		if answer == "" : print "None"
		else:  print answer