"""
@Project Name - main
@author - JOHNATHAN
@date - 6/14/2016
@time - 5:35 PM
@url - https://www.codeeval.com/open_challenges/104/
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
	translate = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
	num = ''
	for word in line.split(';'):
		num += str(translate[word])
	print num