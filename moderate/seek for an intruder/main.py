"""
@Project Name - main
@author - Johnathan
@date - 3/17/2016
@time - 3:26 PM
@url - https://www.codeeval.com/open_challenges/137/

"""

import os
import re
import sys
ips_found = []
dotted_decimal = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
decimal_no_dots = r'\d{4,12}'
dotted_binary = r'[01]{8}\.[01]{8}\.[01]{8}\.[01]{8}'
binary_no_dots = r'[01]{32}'
dotted_hex = r'0x[0-9a-fA-F]{1,2}\.0x[0-9a-fA-F]{1,2}\.0x[0-9a-fA-F]{1,2}\.0x[0-9a-fA-F]{1,2}'
hex_no_dots = r'0x[0-9a-fA-F]{8}'
dotted_octal = r'[0-7]{4}\.[0-7]{4}\.[0-7]{4}\.[0-7]{4}'
octal_no_dots = r'[0-7]{12}'

def is_valid_ip(args):
    # decimal formatted ip
    good_ips = []
    for ip in args:
        if ip == '255.255.255.255': continue
        ip_list = ip.split('.')
        if int(ip_list[0]) < 1: continue
        for x in ip_list:
            if int(x) > 255:  break
        else:
            good_ips.append(ip)
    return good_ips

data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    data = input_file.read().replace('\n','')

ips_found.extend( re.findall(dotted_decimal, data) )
match = re.findall(binary_no_dots, data)
if match:
   converted = [str(int(ip[0:8], 2)) + '.' + str(int(ip[8:16], 2)) + '.' + str(int(ip[16:24], 2)) + '.' + str(int(ip[24:32], 2)) for ip in match]
   ips_found.extend(converted)
print " ".join( is_valid_ip(ips_found) )