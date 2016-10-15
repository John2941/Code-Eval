"""
@Project Name - main
@author - Johnathan
@date - 3/19/2016
@time - 3:15 PM
@url - https://www.codeeval.com/open_challenges/50/

CodeEval gives me no credit, but I cannot find out what is supposedly wrong

"""
import os
import sys

def substitution(master_string, replace_string, sub_string):
    """
    find replace_string and replace it with sub_string as long as the replace_string
        is not between escape characters ( "+" ). If characters are between escape
        characters then that sub string has already been replace once and should
        not be consider again
    :param master_string: the entire string to be searched
    :param replace_string: the sub string to be replace, if it exists
    :param sub_string: the new sub_string to replace replace_string
    :return: new string with new sub_string
    """
    length = len(replace_string)
    escape_character = "+"
    for index in xrange(len(master_string) - length + 1):
        window = master_string[index: length + index]
        if window == replace_string:
            if master_string[:index].count(escape_character) % 2 == 1:
                # means the replace_string is in the middle of a already
                # replaced string
                continue
            new_string = master_string[:index] + escape_character + \
                                sub_string + escape_character + \
                                master_string[index + length:]
            return new_string
    else:
        return None




data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for line in data:
    master_string, changes = line.split(';')
    changes = changes.split(',')
    for c in xrange(0,len(changes),2):
        master_string = substitution(master_string, changes[c], changes[c + 1])\
                        or master_string
    print master_string.replace('+','')