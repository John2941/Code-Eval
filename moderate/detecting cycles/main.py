# -*- coding: utf-8 -*-
"""

Given a sequence, write a program to detect cycles within it.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename containing a sequence of numbers (space delimited). The file can have multiple such lines. E.g


2 0 6 3 1 6 3 1 6 3 1
3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49
1 2 3 1 2 3 1 2 3

OUTPUT SAMPLE:

Print to stdout the first cycle you find in each sequence. Ensure that there are no trailing empty spaces on each line you print. E.g.


6 3 1
49
1 2 3
The cycle detection problem is explained more widely on wiki
Constrains:
The elements of the sequence are integers in range [0, 99]
The length of the sequence is in range [0, 50]


Created on Sat Oct 24 19:07:06 2015

@author: Johnathan
"""

import os
import sys

lines,indexes = [],[]


def dupeElement(_list):
    """
    Iterate over every element in the list to find an exact match

    Return index of both duplicate elements
    """
    matching_indexes = []
    for x in xrange(len(_list)): # iter throught the list
        temp_list = _list[x+1:]
#        breaker = False
        for y in xrange(len(temp_list)): # iter through the remaining of the list searching for matches on the element in the first for loop
            if _list[x] == temp_list[y]:
                first_index = x
                for z in xrange(len(_list)): # iterating through the orginal list to find the index of the matching element, by matching values and making sure the index is higher than the first matched value
                    if z > x and _list[x] == _list[z]:
                        second_index = z
                        matching_indexes.append((first_index,second_index))
#                        breaker = True
                break ## already found all possible matches to the first element so go ahead and break
#                if breaker:
#                    break
    return matching_indexes

def findPattern(list_of_tuples, _list):
    """
    Using the dupeElement output (tuple containing the indexes of matching elements)
    check and see if the element after both matching elements are the same
    and continue comparing (while adding the indexes to the sequence list for the output)
    until there isnt a match
    """
    for _tuple in list_of_tuples:
        if len(_tuple) != 0:
            sequence = []
            for x in xrange(len(_list[_tuple[1]:])):

                if _tuple[0] + x + 1 == _tuple[1]:
                    if len(sequence) == 0:
                        sequence.append(_tuple[0]) ## if match was found but was next element, add it to the list before returning
                    return sequence  # when it has reached the index of the second matching element, break
                try:
                    if _list[_tuple[0] + x + 1] == _list[_tuple[1] + x + 1]:
                        if sequence == []: # when the first match is found populate the first matching index first
                            sequence.append(_tuple[0])
                        sequence.append(_tuple[0] + x + 1 )
                    else:
                        break
                except IndexError: ## incase the matching surpasses the length of the list
                    break
    return sequence



data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    for x in input_file.readlines():#input argv file into list wihtout newline character
        if x != "":
            lines.append(x.strip("\n").split())
    for num_lines in lines:
        num_lines = [int(i) for i in num_lines] #cast elements to ints
#        sys.stdout.write("Orginal Number list: " + str(num_lines) + "\n")
        indexes = findPattern(dupeElement(num_lines),num_lines)
#        sys.stdout.write("Found sequence: ")
        if indexes == []:
            sys.stdout.write("\n")
        else:
            for y in indexes:
                sys.stdout.write(str(num_lines[y]))
                if y != indexes[-1]:
                    sys.stdout.write(" ")
            if num_lines != lines[-1]:
                sys.stdout.write('\n')


















