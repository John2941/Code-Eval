"""
@Project Name - main
@author - Johnathan
@date - 3/14/2017
@time - 6:35 PM
@url - https://www.codeeval.com/open_challenges/93/
"""

import os
import sys

try:
    data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
    with open(data_file, 'r') as input_file:
        data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
    with open(sys.argv[1], 'r') as input_file:
        data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for sentence in data:
    sentence_list = []
    sentence = sentence.split(' ')
    for word in sentence:
        sentence_list.append( word[0].upper() + word[1:] )
    print ' '.join(sentence_list)