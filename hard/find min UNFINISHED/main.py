"""
@Project Name - find min hard
@author - Johnathan
@date - 3/10/2016
@time - 7:31 PM
@url - https://www.codeeval.com/open_challenges/85/

DID NOT FINISH - gives answer but they're incorrect. Not sure if I understand the problem fully
"""

import os
import sys


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		x = x.strip('\n').split(',')
		n = map(int, x)
		n, k, a, b, c, r = n[0], n[1], n[2],  n[3], n[4], n[5]
		known_array = [a]
		for x in xrange(k - 1):
			x = x
			m = (b * known_array[x] + c) % r
			known_array.append(m)
		m = known_array
		for x in xrange(k-(n  - 1) ):
			next_num = 0
			m = sorted(m)
			while True:
				if next_num in m:
					next_num += 1
				else:
					break
			m.append(next_num)
		print m[-1]
