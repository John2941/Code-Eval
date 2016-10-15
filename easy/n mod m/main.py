# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:25:31 2015

Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.

20,6
2,3
You may assume M will never be zero.

OUTPUT SAMPLE:

Print out the value of N Mod M

@author: JOHNATHAN
"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# input_file =  open(sys.argv[1],'r')
input_file =  open(data_file,'r')
line = input_file.readline().strip('\n').split(',')

while True:
    for x in range(10000):
        big = float(line[0])
        mod = float(line[1])
        x = float(x + 1)
        if big/(mod*x) < 1.00000:
            print int(big - (mod * (x - 1)))
            break
    line = input_file.readline().strip('\n').split(',')
    if line[0] == '':
        input_file.close()
        break
    