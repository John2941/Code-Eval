# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:39:42 2015

@author: JOHNATHAN
@url - https://www.codeeval.com/open_challenges/13/
"""

import os
import sys

lines= []

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
        for x in input_file.readlines():#input argv file into list wihtout newline character
            if x != "":            
                lines.append(x.strip("\n"))
        for y in lines:
            remove = [re for re in y.split(',')[1] if re != " "]
            string = y.split(',')[0]
            for z in remove:
                string = string.replace(z,'')
            sys.stdout.write(string + "\n")