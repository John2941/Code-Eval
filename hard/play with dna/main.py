"""
@Project Name - main
@author - JOHNATHAN
@date - 6/21/2016
@time - 1:12 PM
@url - https://www.codeeval.com/open_challenges/126/
"""
class DNA():
	def __init__(self, segment='', mismatch=0, dna=''):
		self.segment = segment
		self.mismatch = int(mismatch)
		self.dna = dna

	def scan_dna(self):
		self.matches = {}
		length = len(self.segment)
		for i in range(len(self.dna))[:-length]:
			seg = self.dna[i:i+length]
			new_seg = self.match_seg(seg)
			if new_seg != None:
				self.matches = self.extend_dict(self.matches, new_seg)
		else:
			return self.matches

	def extend_dict(self, og, new):
		for key in new.keys():
			if key in og.keys():
				og[key].extend(new[key])
			else:
				og[key] = new[key]
		else:
			return og

	def match_seg(self, segment):
		total_mismatched = 0
		for i,letter in enumerate(segment):
			if letter != self.segment[i]:
				total_mismatched += 1
			if total_mismatched > self.mismatch:
				return None
		else:
			return {total_mismatched:[segment]}

	def allowed_matches(self):
		self.scan_dna()
		output = []
		for key in self.matches:
			output.append(' '.join(sorted(self.matches[key])))
		if not output:
			return "No match"
		return ' '.join(output)

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
	segment, mismatch, dna = line.split(' ')
	mismatch = int(mismatch)
	dna = DNA(segment=segment, mismatch=mismatch, dna=dna)
	print dna.allowed_matches()
