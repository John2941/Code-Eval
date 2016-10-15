"""
@Project Name - main
@author - JOHNATHAN
@date - 6/14/2016
@time - 4:51 PM
@url - https://www.codeeval.com/open_challenges/41/
"""

import os
import sys

try:
	data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
	with open(data_file, 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
	with open(sys.argv[1], 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for line in data:
	size, array = line.split(';')
	array = array.split(',')
	for num in array:
		if array.count(num) > 1:
			print num
			break
