"""
@Project Name - main
@author - Johnathan
@date - 3/16/2016
@time - 7:59 PM
@url - https://www.codeeval.com/open_challenges/37/


"""

import os
import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x for x in input_file.read().split('\n') if x]

for x in data:
    not_in = []
    x = x.lower()
    for y in alphabet:
        if y not in x:
            not_in.append(y)
    if not_in:
        print "".join(not_in)
    else:
        print "NULL"