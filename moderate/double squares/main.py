"""
@Project Name - main
@author - Johnathan
@date - 2/7/2017
@time - 9:08 PM

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

def double_squares(_int):



amount, data = data[0], data[1:]

for index in xrange(amount):
    number = data[index]
    print double_squares(number)