"""
@Project Name - test
@author - Johnathan
@date - 3/13/2016
@time - 2:35 PM


"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x.strip('\n') for x in input_file.read().split('\n')]

for x in data:
    print x

