"""
@Project Name - package problem hard
@author - Johnathan
@date - 3/11/2016
@time - 5:03 PM
@url - https://www.codeeval.com/open_challenges/114/
"""
from copy import deepcopy
import os
import sys


def package_combinations(max, possibles=None):
	"""
	:param max: int;  max weight of future package
	:param possibles: list of tuple(3 elements) ; all the possible packages we can choose from
	:return: list of dictionaries (containing all possible additional packages);  a list of all possible combinations
	that we could ship while staying under the max weight
	"""
	combinations = []
	package = {}
	if possibles is None:
		possibles = all_packages
	for i in possibles.keys():
		weight = possibles[i]['weight']
		if weight < max:
			sliced = slicedict(possibles, i)
			difference = max - weight
			package[i] = package_combinations(difference, sliced)
		#if package:  combinations.append(package)
	if not package:
		return None
	return package

def slicedict(dict, exclude):
	#  returns sliced dictionary based on key values higher than the exclude parameter
	return {k:v for k,v in dict.iteritems() if k > exclude}


def highest_priced_package(combinations, tmp=None, recur=False):
	"""
	dictionary recursion is a bitch

	pops are required on the tmp list since lists are mutable so the variable, which should be local
		to that function call, gets modified as if it was a global therefore I have to pop off the last index when done
		with it at the end of the iteration

	deepcopy is required since when trying to assign the value of one dictionary to another variable ( try to create
		a entire new copy) it just passes the reference therefore any changes made to the either one will change the
		value of the other one. deepcopy copies the entire value of one dictionary  into a new variable completely
		independent
	"""
	highest = {0:None}
	global all_packages
	if not combinations: return None
	for k1,v1 in combinations.iteritems():
		index = k1  # single index number of the package in question
		if tmp != None:
		 	tmp.append(index)
		else:
		 	tmp = [index]
		if v1 != None:
			# if there are additional packages nested within this one
			for k2,v2 in v1.iteritems():
				if v2:  # check to see if payload of additional package has packages inside it
					# if it does, add the index of the current package then call the function again
					#   to get to the last package without anymore packages
					higest_tmp = highest_priced_package({k2:v2}, tmp, True)
					if higest_tmp.keys()[0] > highest.keys()[0]:
						highest = deepcopy(higest_tmp)
				else:  # if it does not then add the package to tmp and add the costs
					tmp.append(k2)
					tmp_price = get_cost(tmp)
					if tmp_price.keys()[0] == highest.keys()[0]:
						# same price to ship; need to deteremine lowest weight
						weight_tmp, weight_highest = 0, 0
						for x in tmp_price.values()[0]:
							# get the weight of the newest found packages that has the
							# 	same cost to ship
							weight_tmp += all_packages[x]['weight']
						for x in highest.values()[0]:
							# get the weight of the previous package to ship
							weight_highest += all_packages[x]['weight']
						if weight_tmp < weight_highest:
							# if the newest found package weights less than the previous package to ship then replace
							highest = deepcopy(tmp_price)
					if tmp_price.keys()[0] > highest.keys()[0]:
						# strict comparison of value of the packages to ship
						highest = deepcopy(tmp_price)
					if recur:
						tmp.pop()
						return highest
				tmp.pop()
			tmp = []
		else:
			tmp_price = get_cost(tmp)
			if tmp_price.keys()[0] == highest.keys()[0]:
				# same price to ship; need to deteremine lowest weight
				weight_tmp, weight_highest = 0, 0
				for x in tmp_price.values()[0]:
					weight_tmp += all_packages[x]['weight']
				for x in highest.values()[0]:
					weight_highest += all_packages[x]['weight']
				if weight_tmp < weight_highest:
					highest = deepcopy(tmp_price)
			if tmp_price.keys()[0] > highest.keys()[0]:
					highest = deepcopy(tmp_price)
			tmp.pop()
	return highest

def get_cost(tmp):
	# returns the value of the packages
	tmp_price = 0
	for x in tmp:
		tmp_price += all_packages[x]['price']
	return {tmp_price:tmp}



data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		string_tup = x.strip('\n').split(' : ')
		max_package_weight = int(string_tup[0])
		all_packages = {}  # contains all packages available for shipping
		for w in string_tup[1].split(' '):
			w = w.replace("(","").replace(")","")
			w = w.split(",")
			all_packages[int(w[0])] = {'weight':float(w[1]), 'price':int(w[2].strip("$"))}
		#  potential_packages elements are index
		#print all_packages
		comb = package_combinations(max_package_weight)
		#print comb
		ship = highest_priced_package(comb)
		if ship:
			sys.stdout.write( ",".join([str(x) for x in ship.values()[0]]) + "\n" )
		else:
			sys.stdout.write( "None\n")
