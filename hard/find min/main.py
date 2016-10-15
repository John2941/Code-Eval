"""
@Project Name - find min hard
@author - Johnathan
@date - 3/10/2016
@time - 7:31 PM
@url - https://www.codeeval.com/open_challenges/85/


"""

import os
import sys


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		x = x.strip()
		n, k, a, b, c, r = map(int, x.split(','))
		known_array = [a]
		while 0 < len(known_array) < k:
			m = ((b * known_array[-1]) + c) % r
			known_array.append(m)
		m = known_array
		for x in range(k, n):
			next_num = 0
			while next_num in m:
				next_num += 1
			m.append(next_num)
			m.pop(0)
		print m[-1]


