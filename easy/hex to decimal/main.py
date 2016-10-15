# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:30:44 2015

@author: JOHNATHAN
@url - https://www.codeeval.com/open_challenges/67/
"""

import os
import sys


lines = []


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
        for x in input_file.readlines():#input argv file into list wihtout newline character       
            lines.append(x.strip("\n"))
        for y in lines:
            print int(y,16)
        