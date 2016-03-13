# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:25:31 2015

Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:

The first argument will be a path to a filename containing positive integers, one per line. E.g.

23
496


OUTPUT SAMPLE:

Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

5
19

@author: JOHNATHAN
@url - https://www.codeeval.com/open_challenges/21/
"""

import os
import sys


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# input_file =  open(sys.argv[1],'r')
input_file =  open(data_file,'r')
line = input_file.readline().strip('\n')

while True:
    temp = []
    for x in xrange(len(line)):
        temp.append(x)
    else:
        print sum(temp)

    line = input_file.readline().strip('\n')
    if len(line) == 0:
        input_file.close()
        break
    