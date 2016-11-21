#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created: 2016-11-01
# Author: Johnathan
#
# Distributed under terms of the MIT license.


import os
import sys

try:
    data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
    with open(data_file, 'r') as input_file:
        data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
    with open(sys.argv[1], 'r') as input_file:
        data = [x.strip('\n') for x in input_file.read().split('\n') if x]

change_dict = {
    1: 'PENNY',
    5: 'NICKLE',
    10: 'DIME',
    25: 'QUARTER',
    50: 'HALF DOLLAR',
    100: 'ONE',
    200: 'TWO',
    500: 'FIVE',
    1000: 'TEN',
    2000: 'TWENTY',
    5000: 'FIFTY',
    10000: 'ONE HUNDRED'
}

def change(amount, word_change=None):
    if amount > 0:
        change_keys = change_dict.keys()
        change_keys.sort()
        for x in change_keys[::-1]:
            if amount >= x:
                if not word_change:
                    word_change = []
                word_change.append(change_dict[x])
                change(amount - x, word_change)
                break
    elif amount == 0 and not word_change:
        return ['ZERO']
    return word_change

for line in data:
    total, given = line.split(';')
    if total.count('.'):
        total = int(total.replace('.', ''))
    else:
        total = int(total) * 100
    if given.count('.'):
        given = int(given.replace('.', ''))
    else:
        given = int(given) * 100
    change_amount = given - total
    word_change = change(change_amount)
    if not word_change:
        print "ERROR"
    else:
        print ','.join(word_change)





