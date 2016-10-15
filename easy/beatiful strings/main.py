# -*- coding: utf-8 -*-
"""# -*- coding: utf-8 -*-

When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.

Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it. The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)

You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?

Sample Input
ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves

Output sample
152
754
491
729
646

@author: JOHNATHAN

Created on Sat Oct 24 23:34:12 2015

@author: Johnathan
"""

import os
import sys
lines = []
answer = ''

def alphaCount(_str):
    no_repeat = ''
    repeat_char = {}
    for x in _str.lower():
        if x not in no_repeat and x.isalpha():
            no_repeat += x
    for x in no_repeat:
        count = _str.lower().count(x)
        try:
            repeat_char[count] += x
        except KeyError:
            repeat_char[count] = x
    return repeat_char

def countBeauty(_dict):
    occurences = _dict.keys()
    occurences.reverse()
    max_beauty_points = 26
    accum_point = 0
    for x in occurences: ## iter through the dict keys, which are the number of times a specific letter has been duplicated
        for y in _dict[x]: ## iter through the amount of letters repeated x times
            accum_point += max_beauty_points * x # max_beauty * how many times it was seen in the string
            max_beauty_points -= 1 # dececrement max points since another letter already used it
    return accum_point



data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    for x in input_file.readlines():#input argv file into list wihtout newline character
        if x != "":
            lines.append(x.strip("\n"))
    for line_string in lines:
        win = countBeauty(alphaCount(line_string))
        sys.stdout.write(str(win) + '\n')
















