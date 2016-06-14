"""
@Project Name - main
@author - JOHNATHAN
@date - 6/14/2016
@time - 5:56 PM
@url - https://www.codeeval.com/open_challenges/113/
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
	one, two = line.split(" | ")
	one, two = one.split(' '), two.split(' ')
	one, two = map(int, one), map(int, two)
	total = []
	for i,x in enumerate(one):
		total.append(str(one[i] * two[i]))
	print " ".join(total)
