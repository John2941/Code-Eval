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
    alternate_routes = {}
    used_blocks = []
    restart = True
    totally_not_found = False
    used_alternate_routes = {}
    dont_use_block = {}
    while restart:
        restart = False
        unused_blocks_local = unused_blocks
        used_blocks_local = []
        for index, letter in enumerate(word):
            found = False
            if index not in alternate_routes.keys():
                alternate_routes[index] = {'letter':letter, 'block_index':[]}
            for b_index, blocks in enumerate(unused_blocks):
                if blocks.count(letter):
                    alternate_routes[index]['block_index'].append(b_index)
                    try:
                        temp_key = dont_use_block.keys()[0]
                        if index != temp_key and b_index != dont_use_block[temp_key]:
                            if len(alternate_routes[index]['block_index']) == 1:
                                used_blocks_local.append(blocks)
                                unused_blocks_local.remove(blocks)
                            found = True
                    except IndexError:
                        if len(alternate_routes[index]['block_index']) == 1:
                            used_blocks_local.append(blocks)
                            unused_blocks_local.remove(blocks)
                        found = True
            if not found:
                for routes_index, row in enumerate(alternate_routes):
                    if used_alternate_routes.keys():
                        last_key = alternate_routes.keys()[-1]
                        try:
                            if used_alternate_routes[last_key]['block_index'] == alternate_routes[last_key]['block_index']:
                                totally_not_found = True
                        except KeyError:
                            pass
                    else:
                        totally_not_found = True
                    if len(alternate_routes[routes_index]['block_index']) > 1:
                        if alternate_routes[routes_index] not in used_alternate_routes.keys():
                            used_alternate_routes[routes_index] = {'block_index':[alternate_routes[routes_index]['block_index'][0]]}
                        else:
                            used_alternate_routes[alternate_routes[routes_index]]['block_index'].append(alternate_routes[routes_index]['block_index'][0])
                        dont_use_block = {}
                        dont_use_block[index] = alternate_routes[routes_index]['block_index'][0]
                        restart = True
                        alternate_route_taken = True
                        break
                if not restart or totally_not_found:
                    break
            if totally_not_found:
                restart = False
                break

    count += 1
    print '{} - {}'.format(str(count), found)
    #print found