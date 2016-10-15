"""
@Project Name - main
@author - Johnathan
@date - 4/14/2016
@time - 5:11 PM


"""

import os
import sys

class Prime():
	def __init__(self):
		self.list_of_primes = []
		self.last_prime = self.list_of_primes[-1] if self.list_of_primes else 0

	def list_primes_upto(self, _int):
		if self.last_prime == 0:
			self.generate_primes(_int)
			self.last_prime = self.list_of_primes[-1]
			return self.list_of_primes
		if self.last_prime > _int:
		# find the position in the list_of_primes array thats closest
		#		to the _int
			list_index = self.custom_binary_search(self.list_of_primes, _int)
			self.last_prime = self.list_of_primes[-1]
			return self.list_of_primes[:list_index]
		else:
			self.generate_primes(_int)
			self.last_prime = self.list_of_primes[-1]
			return self.list_of_primes

	def generate_primes(self,_int):
		self.list_of_primes = self.primes(_int)
		self.last_prime = self.list_of_primes[-1]

	def primes(self,n):
		""" Returns  a list of primes < n """
		sieve = [True] * n
		for i in xrange(3,int(n**0.5)+1,2):
			if sieve[i]:
				sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
		return [2] + [i for i in xrange(3,n,2) if sieve[i]]

	def custom_binary_search(self, list, find_int):
		# returns the first index that is either == to find_int or
		#	list[index] > and list[index - 1] <
		low, high = 0, len(list)
		while low <= high:
			half = low + (high - low) / 2
			if find_int == list[half]:
				return half
			elif find_int < list[half]:
				if find_int > list[half - 1]:
					return half
				else:
					high = half - 1
			else: # find_int > list[half}
				if find_int < list[half + 1]:
					return half + 1
				else:
					low = half + 1


try:
	data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
	with open(data_file, 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
	with open(sys.argv[1], 'r') as input_file:
		data = [x.strip('\n') for x in input_file.read().split('\n') if x]

prime = Prime()
list_of_nums = [int(x) for x in data]
highest = sorted(list_of_nums, reverse=True)[0]
prime.generate_primes(highest)
for x in data:
	if int(x) != highest:
		primes = prime.list_primes_upto(int(x))
		print ','.join(str(x) for x in primes)
		#print len(primes)
	else:
		print ','.join(str(x) for x in prime.list_of_primes)
		#print len(prime.list_of_primes)
