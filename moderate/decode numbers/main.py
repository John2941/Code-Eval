"""
@Project Name - main
@author - Johnathan
@date - 3/12/2017
@time - 9:14 AM

url https://www.codeeval.com/open_challenges/73/

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


def decode(message):
    total = 0
    for x in xrange(len(message)):
        if len(message[x: x + 2]) == 2 and int(message[x: x + 2]) < 27:
            total += 1
        if len(message[x + 2:]) > 1:
            total += decode(message[x + 2:])
    return total


for message in data:
    decode_total = 1
    decode_total += decode(message)
    print decode_total