# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:29:33 2015

@author: JOHNATHAN
"""

import os
import sys


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"


#input_file =  open(sys.argv[1],'r')
input_file = open(data_file, 'r')
line = input_file.readline().strip('\n').split(' ')

while True:
    first_div = int(line[0])
    second_div = int(line[1])
    count_till = int(line[2])
    for x in xrange(count_till):
        x += 1
        if x % first_div == 0 and x % second_div == 0:
            sys.stdout.write('FB')
        elif x % first_div == 0:
            sys.stdout.write('F')
        elif x % second_div == 0:
            sys.stdout.write('B')
        else:
            sys.stdout.write(str(x))
        if not (x == count_till):
            sys.stdout.write(' ')
    line = input_file.readline().strip('\n').split(' ')
    if len(line) != 3:
        break
    sys.stdout.write('\n')

        
input_file.close()


        