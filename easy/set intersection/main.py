"""
@Project Name - main
@author - Johnathan
@date - 4/15/2016
@time - 5:25 PM
@url - https://www.codeeval.com/open_challenges/30/

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
	n,z = x.split(';')
	n = n.split(',')
	tmp = []
	for x in z.split(','):
		if x in n:
			tmp.append(x)
	tmp = map(int, tmp)
	tmp = sorted(tmp)
	print ','.join(str(x) for x in tmp)