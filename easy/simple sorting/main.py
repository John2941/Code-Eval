# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:54:02 2015
@url - https://www.codeeval.com/open_challenges/91/
@author: JOHNATHAN
"""
import os
import sys

lines = []

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    for x in input_file.readlines():#input argv file into list wihtout newline character
        lines.append(x.strip("\n"))
    for y in lines: ## iter through all the lines
        sort = y.split(" ")
        for tt in xrange(len(sort)): # convert str to int
            sort[tt] = float(sort[tt])
        sort.sort() # sort list
        for w in xrange(len(sort)): # find the lowest first
            try:
                error_thrower = sort[w+1]
                print "%0.3f" % sort[w],
            except IndexError:
                print "%0.3f" % sort[w]
        
                
            
        