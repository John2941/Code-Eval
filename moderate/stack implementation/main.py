# coding=utf-8
"""
@Project Name - stack implementation
@author - Johnathan
@date - 1/26/2016
@time - 8:19 PM

Write a program which implements a stack interface for integers. The interface should have ‘push’ and ‘pop’ functions. Your task is to ‘push’ a series of integers and then ‘pop’ and print every alternate integer.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains a series of space delimited integers, one per line.

1 2 3 4
10 -2 3 4

OUTPUT SAMPLE:

Print to stdout every alternate space delimited integer, one per line.

4 2
4 -2
"""

import os
import sys


def push(x, stack=[]):
	stack.append(x)
	return stack


def pop(stack):
	return " ".join(stack[::-2])



data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		x = x.strip('\n').split()
		stack = []
		for i in x:
			stack = push(i, stack)
		results = pop(stack)
		sys.stdout.write( results + '\n' )
