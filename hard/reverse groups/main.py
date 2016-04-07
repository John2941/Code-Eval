"""
@Project Name - main
@author - Johnathan
@date - 4/6/2016
@time - 7:13 PM
@url - https://www.codeeval.com/open_challenges/71/
"""
import os
import sys


def organize(_list, k):
	counter = 0
	tmp = []
	while (counter + 1) * k <= len(_list):
		add = _list[counter*k:(counter+1)*k]
		tmp.extend( add[::-1] )
		counter += 1
	tmp.extend( _list[counter*k:] ) # the remaining unsorted
	return tmp

try:
	data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
	with open(data_file, 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
	with open(sys.argv[1], 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
	_list, k = x.split(';')
	k = int(k)
	_list = _list.split(',')
	_list = map(int, _list)
	answer = organize(_list,k)
	sys.stdout.write( ",".join(str(x) for x in answer) + '\n' )
