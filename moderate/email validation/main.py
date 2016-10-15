"""
@Project Name - main
@author - Johnathan
@date - 3/15/2016
@time - 7:54 PM
@url - https://www.codeeval.com/open_challenges/35/


"""

import os
import re
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
    reg = re.compile(r'([^@]+@[^\.]\w+(\.[^\.]\w+)+)') # allows for multiple domains
    #reg = re.compile(r'[^@]+@[^\.]\w+\.[^\.]\w+') # matches basic email addresses
    match = reg.search(x)
    if match:
        if match.group() == x:
            print 'true'
        else:
            print 'false'
    else:
        print 'false'