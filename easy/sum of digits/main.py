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

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x for x in input_file.read().split('\n')]

for x in data:
    tmp = []
    for y in x:
        tmp.append(int(y))
    sys.stdout.write( str(sum(tmp)) + "\n")
