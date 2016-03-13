# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:20:25 2015

@author: JOHNATHAN
"""

import os
import sys

lines,tempa,tempb = [],[],[]

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
        for x in input_file.readlines():#input argv file into list wihtout newline character
            if x != "":            
                lines.append(x.strip("\n"))
        for y in lines:
            tempa = y.split(',')
            tempb = tempa[0].split()
            if tempa[1] == tempb[-1]:
                print "1"
            else:
                print "0"