"""
@Project Name - main
@author - Johnathan
@date - 4/7/2016
@time - 6:07 PM
@url - https://www.codeeval.com/open_challenges/80/

Compare URLs without url library

"""

import os
import sys
import re

def compare_url(url1, url2):
	port_regex = r'\.\w*:(\d{1,5})\/'
	port1 = re.search(port_regex, url1)
	port2 = re.search(port_regex, url2)
	if port1 or port2:
		if port1 and not port2:
			if port1.group(1) != '80':
				# URL2 == default 80 port, url1 is explicitly something different
				return False
		elif port2 and not port1:
			if port2.group(1) != '80':
				# URL1 == default 80 port, url2 is explicitly something different
				return False
		elif port1 and port2:
			if port1.group(1) != port2.group(1):
				# explicit ports on both urls don't match
				return False
		if port1:
			url1 = url1.replace(':' + port1.group(1), '') # removes port from url
		if port2:
			url2 = url2.replace(':' + port2.group(1), '') # removes port from url

	# time to convert special characters
	new_url1 = convert_char(url1)
	new_url2 = convert_char(url2)
	if new_url1.lower() == new_url2.lower():
		# final comparison
		return True
	else:
		return False

def convert_char(url):
	new_url = url[:]
	hex_convert_re = r'%[a-fA-F0-9]{2}'
	url_conversions = re.findall(hex_convert_re, url)
	if url_conversions:
		for x in url_conversions:
			new_url = new_url.replace(x, x[1:].decode('hex'))
	return new_url


# # First attempt was to replace the non standard URL characters with the hex replacement.
# # However, it was better to convert the hex to its original ascii encoding then compare
#
# def convert_char(url):
# 	safe_characters = [',', '/', '?', ':', '@', '&', '=', '+', '$', '#', '.', '%']
# 	new_url = ''
# 	for x in url:
# 		if not x.isalnum() and x not in safe_characters:
# 			new_url += '%' + str(hex(ord(x))[2:])
# 		else:
# 			new_url += x
# 	return new_url



try:
	data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
	with open(data_file, 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
	with open(sys.argv[1], 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
	s1,s2 = x.split(';')
	print compare_url(s1, s2)
