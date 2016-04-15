"""
@Project Name - main
@author - Johnathan
@date - 4/15/2016
@time - 5:45 PM
@url - https://www.codeeval.com/open_challenges/96/

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

for sentence in data:
	new_sent = ''
	for letter in sentence:
		if letter.isalpha():
			if letter.isupper():
				new_sent += letter.lower()
			else:
				new_sent += letter.upper()
		else:
			new_sent += letter
	print new_sent
