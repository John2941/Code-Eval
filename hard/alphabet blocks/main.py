"""
@Project Name - main
@author - Johnathan
@date - 11/3/2016
@time - 6:44 PM

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
count = 0
for line in data:
    block_count, word, blocks = line.split(' | ')
    block_count = int(block_count)
    unused_blocks = blocks.split(' ')
    used_blocks = []
    count += 1
    for letter in word:
        found = False
        for blocks in unused_blocks:
            if blocks.count(letter):
                used_blocks.append(blocks)
                unused_blocks.remove(blocks)
                found = True
                break
        if not found:
            break
    print count,
    print found