"""
@Project Name - main
@author - Johnathan
@date - 3/14/2017
@time - 6:40 PM
@url - https://www.codeeval.com/open_challenges/112/
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
    numbers, swap = line.split(' : ')
    numbers = numbers.split(' ')
    swap = swap.split(', ')
    for instruction in swap:
        instruction = [int(x) for x in instruction.split('-')]
        tmpA = numbers[instruction[0]]
        tmpB = numbers[instruction[1]]
        numbers[instruction[0]] = tmpB
        numbers[instruction[1]] = tmpA
    print ' '.join(numbers)