"""
@Project Name - main
@author - Johnathan
@date - 11/1/2016
@time - 9:31 PM

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


def create_array(row, columns, _list):
    array = []
    for r in xrange(row):
        array.append(_list[r * columns: (r + 1) * columns])
    return array

def is_array_empty(array):
    for r in xrange(len(array)):
        for c in xrange(len(array[0])):
            if array[r][c] != '@':
                return False
    else:
        return True
def spiral(array):
    possible_moves = [[0,1],[1,0],[0,-1],[-1,0]]
    current_index = [0, 0]
    word = [array[current_index[0]][current_index[1]]]
    array[current_index[0]][current_index[1]] = '@'
    last_move = []
    while True:
        for index, move in enumerate(possible_moves):
            try:
                if last_move:
                    if array[(current_index[0] + last_move[0])][(current_index[1] + last_move[1])]:
                        move = last_move
                    else:
                        last_move = []
            except IndexError:
                pass
            try:
                selection = array[(current_index[0] + move[0])][(current_index[1] + move[1])]
            except IndexError:
                continue
            if selection != '@':
                word.append(selection)
                last_move = move
                array[current_index[0] + move[0]][current_index[1] + move[1]] = '@'
                current_index[0] = current_index[0] + move[0]
                current_index[1] = current_index[1] + move[1]
                break
            if index == (len(possible_moves) - 1):
                if is_array_empty(array):
                    return word
                else:
                    last_move = []

def print_array(array):
    largest_len = 0
    for r in array:
        for c in r:
            if len(c) > largest_len:
                largest_len = len(c)
    for r in array:
        for c in r:
            print c.ljust(largest_len + 1),
        print ''

for line in data:
    rows, columns, _list = line.split(';')
    rows = int(rows)
    columns = int(columns)
    _list = _list.split(' ')
    array = create_array(rows, columns, _list)
    #print_array(array)
    #print '-' * 25
    word = spiral(array)
    print ' '.join(word)
    #print '=' * 25
