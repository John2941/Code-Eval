"""
@Project Name - main
@author - Johnathan
@date - 3/14/2017
@time - 6:24 PM

@url - https://www.codeeval.com/open_challenges/222/

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


for line in data:
    names, number = line.split(' | ')
    number = int(number)
    names = names.split(' ')
    while len(names) != 1:
        pop_index = (number % len(names)) - 1
        names.pop(pop_index)
    print names[0]