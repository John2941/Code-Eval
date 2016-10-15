"""
@Project Name - Minesweeper Hard
@author - Johnathan
@date - 3/7/2016
@time - 7:05 PM
@url - https://www.codeeval.com/open_challenges/79/

You will be given an M*N matrix. Each item in this matrix is either a '*' or a '.'. A '*' indicates a mine whereas a '.' does not. The objective of the challenge is to output a M*N matrix where each element contains a number (except the positions which actually contain a mine which will remain as '*') which indicates the number of mines adjacent to it. Notice that each position has at most 8 adjacent positions e.g. left, top left, top, top right, right, ...

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains M,N, a semicolon and the M*N matrix in row major form. E.g.

3,5;**.........*...
4,4;*........*......

OUTPUT SAMPLE:

Print out the new M*N matrix (in row major form) with each position(except the ones with the mines) indicating how many adjacent mines are there. E.g.

**100332001*100
*10022101*101110

"""

import os
import sys

def break_into_array(game_input, row_length, col_length):
	output, tmp = [], []
	for index in xrange(col_length):
		output.append([game_input[index * row_length:(index + 1) * row_length]])
	return output

def mine_neighbor_count(array, game_input, row_length, col_length):
	"""
	Examples are set with the given parameters
	array, '**.........*...', 3, 5
	"""
	length = len(game_input)
	output_num = ''
	for x in xrange(length):
		num_of_mines = 0
		position = x + 1
		row_num = x / row_length  # 0 0 0 1 1 1 2 2 2 3 3 3 4 4 4
		col_num = x % row_length  # 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2
		if game_input[x] == "*":
			output_num += "*"
			continue
		if col_num > 0:
			#  left
			if array[row_num][0][col_num - 1] == "*":	num_of_mines += 1
		if col_num < (row_length - 1):
			#  right
			if array[row_num][0][col_num + 1] == "*":	num_of_mines += 1
		if row_num > 0:
			#  deals with top of the array
			if array[row_num - 1][0][col_num] == "*":	num_of_mines += 1
			if col_num > 0:
				#top left
				if array[row_num - 1][0][col_num - 1] == "*":	num_of_mines += 1
			if col_num < row_length - 1:
				# top right
				if array[row_num - 1][0][col_num + 1] == "*":	num_of_mines += 1
		if row_num < col_length - 1:
			#  deals with bottom of the array
			if array[row_num + 1][0][col_num] == "*":	num_of_mines += 1
			if col_num > 0:
				#  bottom left
				if array[row_num + 1][0][col_num - 1] == "*":	num_of_mines += 1
			if col_num < row_length - 1:
				#  bottom right
				if array[row_num + 1][0][col_num + 1] == "*":	num_of_mines += 1
		output_num += str(num_of_mines)
	return output_num


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		x = x.strip('\n')
		x = x.split(',')
		col = x[0]
		x = x[1].split(';')
		row, game = x[0], x[1]
		array = break_into_array(game, int(row), int(col))
		print mine_neighbor_count(array, game, int(row), int(col))

