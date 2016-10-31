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


def decode(letter):
    if 96 < ord(letter) < 103:
        decoded_letter = chr(ord(letter) + 20)
    elif 116 < ord(letter) < 123:
        decoded_letter = chr(ord(letter) - 20)
    elif 102 < ord(letter) < 110:
        decoded_letter = chr(ord(letter) + 7)
    else:
        decoded_letter = chr(ord(letter) - 7)
    return decoded_letter

for line in data:
    for letter in line:
        #print '{0} -> {1}'.format(letter, decode(letter))
        sys.stdout.write(decode(letter))
    print ''
