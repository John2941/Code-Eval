"""
@Project Name - main
@author - Johnathan
@date - 3/15/2016
@time - 8:17 PM
@url - https://www.codeeval.com/open_challenges/28/

"""

import os
import sys


def match(substring, master_string):
    if '\\' in substring or '*' in substring:
        length = len(substring.replace("\\",'').replace('*',''))
    else:
        length = len(substring)
    for master_index in xrange(len(master_string) - length + 1):
        escaped_ask = False
        wild_card_in_effect = False
        escape_length_sup = 0
        wild_card_matched_zero_char = 0
        wild_card_first_match = False
        for sub_index in xrange(len(substring)):
            single_str = substring[sub_index]
            #master_str = master_string[(master_index - (escape_length_sup + wild_card_matched_zero_char)) + sub_index]
            if wild_card_in_effect:
                if wild_card_first_match and substring[sub_index] == master_string[(master_index - (1 + escape_length_sup + wild_card_matched_zero_char)) + sub_index]:
                    wild_card_matched_zero_char += 1
                    wild_card_in_effect = False
                if substring[sub_index] == master_string[(master_index - (escape_length_sup + wild_card_matched_zero_char)) + sub_index]:
                    wild_card_in_effect = False
                wild_card_first_match = False
                continue
            if substring[sub_index] == "\\" and substring[sub_index + 1] == '*' and not escaped_ask:
                escape_length_sup += 1
                escaped_ask = True
                continue
            if substring[sub_index] == "*" and not escaped_ask:
                # wild card, dont have to compare
                wild_card_in_effect = True
                wild_card_first_match = True
                continue
            if substring[sub_index] == "*" and escaped_ask:
                escaped_ask = False
                if substring[sub_index] != master_string[(master_index - (escape_length_sup + wild_card_matched_zero_char)) + sub_index]:
                    break
            if substring[sub_index] != master_string[(master_index - (escape_length_sup + wild_card_matched_zero_char)) + sub_index]:
                break
        else:
            if wild_card_in_effect:
                # if the wild card matched the rest of the word then make sure the
                #   end of the substring was in the master string
                # i.e., C**dfgdfgvalEval,C\**Eval == MATCH; C**dfgdfgval,C\**Eval does NOT match
                end_of_substring = substring.split("*")[-1]
                if end_of_substring:
                    if end_of_substring != master_string[-1 * len(end_of_substring):]:
                        return False
            return True
    return False


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
    _str, sub = x.split(',')
    is_match = match(sub, _str)
    if is_match:
        print 'true'
    else:
        print 'false'