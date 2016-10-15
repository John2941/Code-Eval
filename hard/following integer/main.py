"""
@Project Name - Following Integer Hard
@author - Johnathan
@date - 3/6/2016
@time - 4:09 PM

FOLLOWING INTEGER
CHALLENGE DESCRIPTION:

Credits: This challenge has appeared in a past google competition

You are writing out a list of numbers.Your list contains all numbers with exactly Di digits in its decimal representation which are equal to i, for each i between 1 and 9, inclusive. You are writing them out in ascending order. For example, you might be writing every number with two '1's and one '5'. Your list would begin 115, 151, 511, 1015, 1051. Given N, the last number you wrote, compute what the next number in the list will be. The number of 1s, 2s, ..., 9s is fixed but the number of 0s is arbitrary.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10^6. E.g.

115
842
8000

OUTPUT SAMPLE:

151
2048
80000
"""
import os
import sys

def parse_changing_index(number):
	"""
	:param number: str format of a number
	:return: the number and index of the number that needs to move for the next number in that sequence
	"""
	if number == "".join(sorted(number, reverse=True)):
		return None
	number = number[::-1]
	previous_num = number[0]
	for index,x in enumerate(number):
		if index == 0:
			continue
		if int(x) < int(previous_num):
			return len(number) - index - 1# this is index in reverse
		previous_num = x


def find_rearragement(changing_index, number):
	num_prefix = number[:changing_index]
	num = number[changing_index]
	num_postfix = number[changing_index + 1:]
	new_num = sorted(num_postfix)[0]  # retrieve smallest number after the changing number (not to include that num)
	num_postfix = sorted(num_postfix)[1:]
	num_postfix.append(num)
	return num_prefix + new_num + "".join(sorted(num_postfix))

def add_zero(number):
	number = number[::-1]
	prefix = number[0]
	index = 0
	for x in xrange(len(number)):
		if number[x] == '0':
			continue
		prefix = number[x]
		index = x
		break
	postfix = number[:index] + number[index + 1:]
	return prefix + '0' + "".join(sorted(postfix))



data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	data = input_file.read()
data = data.split('\n')
for x in data:
	if len(x) > 0:
		if x == '0':
			sys.stdout.write('00' + '\n')
			continue
		indexes = parse_changing_index(x)
		if indexes != None:
			sys.stdout.write(find_rearragement(indexes, x) + "\n")
		else:
			sys.stdout.write(add_zero(x) + '\n')
