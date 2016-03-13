"""
@Project Name - string list hard
@author - Johnathan
@date - 2/6/2016
@time - 5:14 PM

STRING LIST
CHALLENGE DESCRIPTION:

Credits: Challenge contributed by Max Demian.

You are given a number N and a string S. Print all of the possible ways to write a string of length N from the characters in string S, comma delimited in alphabetical order.

INPUT SAMPLE:

The first argument will be the path to the input filename containing the test data. Each line in this file is a separate test case. Each line is in the format: N,S i.e. a positive integer, followed by a string (comma separated). E.g.

1,aa
2,ab
3,pop

OUTPUT SAMPLE:

Print all of the possible ways to write a string of length N from the characters in string S comma delimited in alphabetical order, with no duplicates. E.g.

a
aa,ab,ba,bb
ooo,oop,opo,opp,poo,pop,ppo,ppp
"""

import os
import sys


def iterate(word, length):
	iter_count = [0 for x in range(length)]
	final_output = []
	while iter_count:
		temp = ''
		for x in iter_count:
			temp += word[x]
		if temp not in final_output:
			final_output.append(temp)
		iter_count = increment_array(iter_count[::-1],length)
	sys.stdout.write( ','.join(final_output) + '\n' )


def increment_array(array, length):
	change_array = array
	for x in xrange(len(change_array)):
		if change_array[x] == length - 1:
			change_array[x] = 0
			try:
				if change_array[x + 1] == length - 1:
					continue
				else:
					change_array[x + 1] = change_array[x + 1] + 1
					return change_array[::-1]
			except IndexError:
				return False
		change_array[x] = change_array[x] + 1
		return change_array[::-1]





data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		length, word = x.split(',')
		word = ''.join(sorted(word))
		if int(length) > len(word):
			length = len(word)
		iterate(word.strip('\n'), int(length))