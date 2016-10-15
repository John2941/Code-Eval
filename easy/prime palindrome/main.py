"""
@Project Name - main
@author - Johnathan
@date - 4/15/2016
@time - 5:13 PM
@url - https://www.codeeval.com/open_challenges/3/

"""
import math

def primes(n):
	""" Returns  a list of primes < n """
	sieve = [True] * n
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def is_palindrome(n):
	n = str(n)
	if len(n) % 2 == 0:
		if n[:len(n)/2] == n[len(n)/2:][::-1]:
			return True
	else:
		if n[:len(n)/2] == n[int(math.ceil(len(n)/2.0)):][::-1]:
			return True
	return False


prime_list = primes(1000)
for x in prime_list[::-1]:
	if is_palindrome(x):
		print x
		break