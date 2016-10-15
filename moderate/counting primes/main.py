"""
@Project Name - main
@author - Johnathan
@date - 10/12/2016
@time - 7:10 PM

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

def is_prime(_int):
    if _int == 2 or _int == 3:
        return True
    if _int % 3 == 0 or _int < 2 or _int % 2 == 0:
        return False
    x = 3
    while x <= _int/2:
        if _int % x == 0:
            return False
        x += 2
    return True

for line in data:
    first_int, second_int = map(int, line.split(','))
    counter = 0
    while first_int < second_int:
        if is_prime(first_int):
            counter += 1
        first_int += 1
    print counter
