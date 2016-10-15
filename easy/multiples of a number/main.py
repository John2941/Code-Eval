"""
@Project Name - main
@author - Johnathan
@date - 3/15/2016
@time - 5:36 PM
@url - https://www.codeeval.com/open_challenges/18/


"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
    num, multiple = x.split(',')
    num, multiple = int(num), int(multiple)
    counter = 1
    while True:
        compare = multiple * counter
        if compare > num:
            print compare
            break
        counter += 1