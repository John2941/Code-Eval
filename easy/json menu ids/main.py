"""
@Project Name - JSON Menu IDs Hard
@author - Johnathan
@date - 2/29/2016
@time - 7:28 PM

https://www.codeeval.com/open_challenges/102/

"""
import json
import os
import sys


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		x = x.strip('\n')
		if x == "":
			continue
		x = json.loads(x)
		if x['menu']['items'][0]:
			sum = 0
			for y in x['menu']['items']:
				try:
					if 'label' in y.keys():
						sum += y['id']
				except AttributeError:
					pass
			sys.stdout.write( str(sum) + '\n' )