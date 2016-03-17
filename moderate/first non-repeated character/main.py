"""
@Project Name - main
@author - Johnathan
@date - 3/16/2016
@time - 8:16 PM
@url - https://www.codeeval.com/open_challenges/12/

"""

import os
import sys

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for word in data:
    for x in xrange(len(word)):
        if word[x] in word[:x] or word[x] in word[x + 1:]:
            continue
        print word[x]
        break
    else:
        print None