# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:37:15 2015

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1. Given an integer n≥0, print out the F(n).

INPUT SAMPLE:

The first argument will be a path to a filename containing integer numbers, one per line. E.g.

5
12
OUTPUT SAMPLE:

Print to stdout, the fibonacci number, F(n). E.g.

5
144

@author: Johnathan
"""

import os
import sys

lines = []

def fib(how_many):
    fib_list = [1,1]
    if how_many == 0:
        return 0
    while len(fib_list) < how_many:
        fib_list.append(fib_list[-2] + fib_list[-1])
    else:
        return fib_list[-1]

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    for x in input_file.readlines():#input argv file into list wihtout newline character
        if x != "":
            lines.append(x.strip("\n"))
    for x in lines:
        sys.stdout.write(str(fib(int(x))) + "\n")