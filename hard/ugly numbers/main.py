"""
@Project Name - main
@author - Johnathan
@date - 3/19/2016
@time - 6:04 PM
@url - https://www.codeeval.com/open_challenges/42/

still getting wrong amount of uglies for 12345

"""

import os
import sys

def generate_num_combos(number):
	og_num = str(number)
	number = str(number)
	combos = []
	for a in xrange(len(number)):
		# revolves around the number; 123 -> 231 -> 312
		#number = og_num[a:] + og_num[:a]
		pass
	split = [str(len(number))]
	combos.append((number,))
	finished = ['1'] * len(number)
	i = 1
	while split != finished:
		# while calculates all possible index configurations
		if int(split[-i]) > 1:
			#list(set(split[-i + 1:])) == ['1'] or len(split) == 1
			if i == 1:
				split[-i] = str(int(split[-i]) - 1)
				split.append('1')
			else:
				split[-i] = str(int(split[-i]) - 1)
				split[-i + 1] = str(int(split[-i + 1]) + 1)
			i = 1
			tmp = 0
			_list = []
			for x in split:
				# appends the index configuration using the values at the
				#   specified indexes from number
				_list.append(number[tmp:tmp + int(x)])
				tmp += int(x)
			combos.append(tuple(_list))
		else:
			i += 1
	return combos


def generate_arithmetic(combinations):
	# only doing addition and subtration
	# arithmetic combinations will be generated with 1 for + and 0 for -
	sum_of_combos = []
	for sets_of_nums in combinations:
		num_of_art = len(sets_of_nums) - 1
		finished = ['1'] * num_of_art
		config = ['0'] * num_of_art
		i = 1
		while config != finished:
			if config[-i] == '0':
				sum_of_combos.append( arithmetic(sets_of_nums, config) )
				#print config,
				if i == 1:
					config[-1] = '1'
				else:
					config = config[:-i]
					config.append('1')
					config.extend(['0'] * (i - 1) )
					i = 1
					continue
			i += 1
		sum_of_combos.append( arithmetic(sets_of_nums, finished) )
	return sum_of_combos


def arithmetic(numbers, art_combo):
	if len(numbers) == 1: return int(numbers[0])
	if art_combo[0] == '1':
		total = int(numbers[0]) + int(numbers[1])
	else:
		total = int(numbers[0]) - int(numbers[1])
	if len(art_combo) > 1:
		for index in xrange(1,len(art_combo)):
			if art_combo[index] == '1':
				total += int(numbers[index + 1])
			else:
				total -= int(numbers[index + 1])
	return total

def number_of_uglies(list_of_num):
	total = 0
	for x in list_of_num:
		if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
			total += 1
	return total

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
	num_combos = generate_num_combos(x)
	sums = generate_arithmetic(num_combos)
	#print sums,
	print number_of_uglies(sums)


