"""
@Project Name - main.py
@author - Johnathan
@date - 3/13/2016
@time - 2:01 PM
@url - https://www.codeeval.com/open_challenges/191/


"""

import os

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as f:
    data = [x.strip('\n') for x in f.read().split('\n')]

for x in data:
    print x
