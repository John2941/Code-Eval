#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created: 2016-10-30
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


for line in data:
    longest_word = ''
    for word in line.split(' '):
        if len(word) > len(longest_word):
            longest_word = word
    else:
        print longest_word
