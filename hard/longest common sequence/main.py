"""
@Project Name - Longest Common Sequence Hard
@author - Johnathan
@date - 2/29/2016
@time - 7:52 PM

LONGEST COMMON SUBSEQUENCE
CHALLENGE DESCRIPTION:

You are given two sequences. Write a program to determine the longest common subsequence between the two strings (each string can have a maximum length of 50 characters). NOTE: This subsequence need not be contiguous. The input file may contain empty lines, these need to be ignored.

INPUT SAMPLE:

The first argument will be a path to a filename that contains two strings per line, semicolon delimited. You can assume that there is only one unique subsequence per test case. E.g.

XMJYAUZ;MZJAWXU
OUTPUT SAMPLE:

The longest common subsequence. Ensure that there are no trailing empty spaces on each line you print. E.g.

MJAU

"""

import os
import sys



def common_array(letter, index):
	if not array:
		add_to_array = {}
		add_to_array[index] = letter
		array.append(add_to_array)
		last_set = (index, letter)
	else:
		tmp_array = []
		for x in array:  # iterate through the array
			last_index = list(x.keys())
			if index > last_index[-1]:  # view last item added
				x[index] = letter
				continue
			else:
				new_array = {}
				for y in x:  # iterate through array item
					if y < index:
						new_array[y] = x[y]
					else:
						new_array[index] = letter
						continue
			if new_array not in tmp_array:
				tmp_array.append(new_array)
		for x in tmp_array:
			array.append(x)


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		array = []
		already_used = {}
		x = x.strip('\n').split(';')
		for ind, y in enumerate(x[0]):
			if y in x[1]:
				try:
					try:
						last_used = x[1].index(y, already_used[y][-1] + 1)
					except KeyError:
						last_used = x[1].index(y)
					except ValueError:
						continue  # no addition letters of that kind left
					if already_used[y]:
						already_used[y].append(last_used)
				except KeyError:
					already_used[y] = [last_used]
				common_array(y, last_used)
		largest_array_index = (0,0)  # index,length
		for index,x in enumerate(array):
			if len(x) > largest_array_index[1]:
				largest_array_index = (index,len(x))
		sys.stdout.write("".join(array[largest_array_index[0]].values()).strip(' ') + '\n')