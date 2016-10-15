"""
@Project Name - main
@author - JOHNATHAN
@date - 6/14/2016
@time - 5:48 PM
@url - https://www.codeeval.com/open_challenges/103/
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

for x in data:
	array = x.split(' ')
	for num in sorted(set(array)):
		if array.count(num) == 1:
			print array.index(num) + 1
			break
	else:
		print '0'
