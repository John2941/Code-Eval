# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:20:25 2015

@author: JOHNATHAN
"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
        for x in input_file.readlines():#input argv file into list wihtout newline character
            if x != "":            
                msg, word = x.strip('\n').split(',')
                if msg[-1 * len(word):] == word:
                    sys.stdout.write( '1\n' )
                else:
                    sys.stdout.write( '0\n' )