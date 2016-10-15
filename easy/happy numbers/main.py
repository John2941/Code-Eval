"""
@Project Name - main
@author - Johnathan
@date - 4/15/2016
@time - 5:35 PM
@url - https://www.codeeval.com/open_challenges/39/

"""

import os
import sys


def is_happy(n):
	count = 0
	while count < 1000:
		str_n = str(n)
		sum_total = 0
		for x in str_n:
			sum_total += int(x)**2
		if sum_total == 1:
			return True
		n = sum_total
		count += 1
	return False

try:
	data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
	with open(data_file, 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
	with open(sys.argv[1], 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
	print int(is_happy(int(x)))
