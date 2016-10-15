# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:57:41 2015

@author: JOHNATHAN
"""


import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x for x in input_file.read().split('\n') if x]
    for y in data:
        biggest = 0
        first_list = y.split(',')
        for index,num in enumerate(first_list):
            for num2 in xrange(len(first_list[index:])):
                sum_list = sum([int(num4) for num4 in first_list[index: num2 + index + 1]])
                if sum_list > biggest:
                    biggest = sum_list
        sys.stdout.write(str(biggest) + "\n")