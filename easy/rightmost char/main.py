"""
@Project Name - main
@author - Johnathan
@date - 4/15/2016
@time - 5:29 PM
@url - https://www.codeeval.com/open_challenges/31/

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
	sentence, letter = x.split(',')
	sentence = sentence[::-1]
	index = sentence.find(letter) or -1
	if index != -1:
		print len(sentence) - index - 1
	else:
		print index