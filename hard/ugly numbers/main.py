"""
@Project Name - main
@author - Johnathan
@date - 3/19/2016
@time - 6:04 PM
@url - https://www.codeeval.com/open_challenges/42/

did not receive all credit, not sure what areas are wrong.

"""

import os
import sys

def generate_num_combos(number):
	"""
	ALL EXAMPLES DONE WITH NUMBER = 7
	:param number:
	:return: a list of all number configurations that will be used to add
				and/or subtract
	"""
	len_num = len(str(number))
	number_pre_premutations = [[str(len_num)],[str(len_num - 1), '1']] # initializes with [7,61]
	index = 1
	while number_pre_premutations[-1] != ['1'] * len(str(number)):
		current_perm = number_pre_premutations[-1]
		set_list = set(current_perm[1:])
		if list(set_list) == ['1']:
			new_first_num = [str(int(current_perm[0]) - 1)]
			while True:
				current_sum = sum(int(x) for x in new_first_num)
				if int(new_first_num[0]) > len_num / 2:
					new_first_num.append( str(len_num - int(new_first_num[0])) )
					number_pre_premutations.append(new_first_num)
					break
				elif current_sum == len_num:
					number_pre_premutations.append(new_first_num)
					break
				elif current_sum + int(new_first_num[0]) > len_num:
					new_first_num.append( str(len_num - current_sum) )
					number_pre_premutations.append(new_first_num)
					break
				else:
					new_first_num.append( new_first_num[0] )
			index = 1
			continue
		if current_perm[-index] != '1':
			if index == 1:
				current_perm = [current_perm[:-index][0], str(int(current_perm[-index]) - 1)]
			else:
				prev_current_perm = current_perm
				current_perm = [current_perm[:-index][0], str(int(current_perm[-index]) - 1)]
				current_perm.extend(prev_current_perm[-(index -1):])
			current_perm.append( '1' )
			index = 1
			number_pre_premutations.append(current_perm)
		else:
			index += 1
	number_pre_premutations = combinations_of_perms( number_pre_premutations)
	real_num_perms = change_index_to_actual_numbers( number_pre_premutations, number )
	return real_num_perms

def combinations_of_perms(_list):
	all_perms = [_list[0]]
	for elements in _list[1:]:
		# if len(elements) == 1:
		# 	all_perms.append(elements)
		# 	continue
		last = None
		# skip successive numbers
		for x in xrange(len(elements)):
			add = elements[x:] + elements [:x]
			if add not in all_perms:
				all_perms.append( add )
			last = elements[x]

	return all_perms

def change_index_to_actual_numbers(index_perms, number):
	real_num_perms = [[number]]
	for element in index_perms[1:]:
		# skip first one because its the entire number
		real_num = []
		index_count = 0
		for index in element:
			real_num.append( number[index_count: index_count + int(index)] )
			index_count += int(index)
		real_num_perms.append(real_num)
	return real_num_perms


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
					# Means the subtraction and addition operation has already been
					#	preformed.
					config[-1] = '1'
				else:
					config = config[:-i] # maybe -(i+1)
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


try:
	data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
	with open(data_file, 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
	with open(sys.argv[1], 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
	#print x
	if len(x) == 1:
		print number_of_uglies( [int(x)] )
	else:
		num_combos = generate_num_combos( x )
		sums = generate_arithmetic(num_combos)
		print number_of_uglies(sums)

