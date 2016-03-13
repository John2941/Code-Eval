# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:06:53 2015

@author: JOHNATHAN
"""

import os
import sys


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# input_file =  open(sys.argv[1],'r')
input_file =  open(data_file,'r')
line = input_file.readline().strip('\n').split(' ')
output = ''
while True:
    for x in range(len(line)):
        output += line[(len(line)-(x+1))]
        if (x + 1) != len(line):
            output += ' '
    print output
    output = ''
    line = input_file.readline().strip('\n').split(' ')
    if len(line) <= 1:
        break

