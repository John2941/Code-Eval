"""
@Project Name - main
@author - Johnathan
@date - 3/16/2016
@time - 8:07 PM
@url - https://www.codeeval.com/open_challenges/27/

"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
    if int(x) >= 0:
        bin_num = bin(int(x))[2:]
        for x in xrange(len(bin_num)):
            if bin_num[x] == '1':
                print bin_num[x:]
                break
    else:
        print ''
