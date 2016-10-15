"""
@Project Name - main
@author - Johnathan
@date - 3/16/2016
@time - 7:55 PM
@url - https://www.codeeval.com/open_challenges/16/

"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
    ones = [int(x) for x in bin(int(x)) if x == '1']
    print sum(ones)