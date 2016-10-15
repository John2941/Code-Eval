"""
@Project Name - main
@author - Johnathan
@date - 3/27/2016
@time - 3:08 PM
@url - https://www.codeeval.com/open_challenges/197/

"""
import os
import math
import sys

def columns(_int):
	if _int == 0: return None
	if _int < 27: return (chr(_int + 64), _int)
	number = int(_int)
	x = 0
	tmp = 0
	while True:
		tmp += 26 ** x
		if number >= tmp:
			x+=1
		else:
			break
	num_of_col = x
	column_title = ""
	for x in range(num_of_col)[::-1]:
		if (number <= 26**x and x != 0) or number == 0:
			column_title += 'A'
			continue
		tmp = float(number ) / (26.0 ** float(x))
		if tmp.is_integer() or  tmp > 26.0:
			if tmp >= 27:
				column_character_num = int(tmp) -1
			else:
				if x != num_of_col -1:
					column_character_num = int(tmp)
				else:
					column_character_num = int(math.ceil(tmp)) - 1
		else:
			column_character_num = int(tmp)
		number -=((26**x) * column_character_num)
		column_title += chr(column_character_num + 64)
	return (column_title, _int)

try:
	data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
	with open(data_file, 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
	with open(sys.argv[1],'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
	print columns(int(x))

