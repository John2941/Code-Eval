"""
@Project Name - main
@author - JOHNATHAN
@date - 6/14/2016
@time - 5:07 PM
@url - https://www.codeeval.com/open_challenges/43/
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
	array = map(int, array)
	size = len(array)
	for index,num in enumerate(array[1:]):
		absolute = abs(array[index] - array[index - 1])
		if absolute > size:
			print "Not jolly"
			break
	else:
		print "Jolly"

