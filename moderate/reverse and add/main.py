"""
@Project Name - Reverse and Add moderate
@author - Johnathan
@date - 2/7/2016
@time - 5:02 PM

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla
The problem is as follows: choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure.

For example:

195 (initial number) + 591 (reverse of initial number) = 786

786 + 687 = 1473

1473 + 3741 = 5214

5214 + 4125 = 9339 (palindrome)
In this particular case the palindrome 9339 appeared after the 4th addition. This method leads to palindromes in a few step for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It is not proven though, that there is no such a palindrome.

INPUT SAMPLE:

195

OUTPUT SAMPLE:

For each line of input, generate a line of output which is the number of iterations (additions) to compute the palindrome and the resulting palindrome. (they should be on one line and separated by a single space character).

4 9339
"""

import os
import sys


def is_palindrome(str_number):
	if str_number[:len(str_number) / 2] == str_number[len(str_number) / 2 * -1:][::-1]:
		return True
	return False



data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		x = x.strip('\n')
		for x in x.split(' '):
			temp = x[:]
			palindrome_bool = is_palindrome(temp)
			total = temp
			counter = 0
			while not palindrome_bool:
				one_num = int(temp)
				two_num = int(temp[::-1])
				total = one_num + two_num
				temp = str(total)
				counter += 1
				palindrome_bool = is_palindrome(temp)
				if counter > 100:
					break
			sys.stdout.write(str(counter) + ' ' + str(total) + '\n')
