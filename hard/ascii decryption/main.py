"""
@Project Name - ascii decryption
@author - Johnathan
@date - 1/26/2016
@time - 8:53 PM

You are an analyst at the Central Intelligence Agency, and you have intercepted a top secret encrypted message which contains numbers. Each number is obtained by taking an ASCII code of the original character and adding some unknown constant N.

For example, you can encrypt the word 'test' with the condition that N = 11.

'test' to ASCII -> 116 101 115 116 -> add N to each number-> 127 112 126 127

Based on previous intelligence reports, you know that the original message includes two identical words consisting of X characters and you know the last letter in the word.

Your challenge is to decrypt the message.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.

Each line of input consists of three parts: length of a word, which is repeated twice, the last letter of this word, and an encrypted message separated with space:



5 | s | 92 112 109 40 118 109 109 108 123 40 119 110 40 124 112 109 40
117 105 118 129 40 119 125 124 127 109 113 111 112 40 124 112 109 40
118 109 109 108 123 40 119 110 40 124 112 109 40 110 109 127 54 40 53
40 91 120 119 107 115

OUTPUT SAMPLE:

For each line of input print out decrypted message:


The needs of the many outweigh the needs of the few. - Spock


"""

import sys
import os


class AsciiDecode(object):

	def __init__(self, combined_input):
		self.combined_input = combined_input.split('|')
		self.len_of_hint = int(self.combined_input[0])
		self.last_char = self.combined_input[1].strip()
		self.encrypted_msg = [int(x) for x in self.combined_input[2].split()]
		self.word_found = self.find_hint()
		self.key = self.word_found[-1] - ord(self.last_char)
		self.decoded_ascii_message = self.decode()
		self.decoded_text_message = self.translate_ascii()


	def __repr__(self):
		return self.decoded_text_message

	def find_hint(self):
		for x in xrange(len(self.encrypted_msg[:(self.len_of_hint * -1)])):
			# This iteration grabs the guess and looks for a match in the next iteration
			iter_guess = self.encrypted_msg[x:x+self.len_of_hint + 2]
			for y in xrange(len(self.encrypted_msg[x + 1:(self.len_of_hint * -1) + -1])):
				second_iter = self.encrypted_msg[y + x + 1:y+ + x + 3 + self.len_of_hint]
				if second_iter == iter_guess and second_iter[0] == second_iter[-1]:
					# Compare the guesses and make sure spaces are not included
					self.space_key = self.encrypted_msg[x + y]
					return second_iter[1:-1]

	def decode(self):
		tmp_msg = []
		for x in self.encrypted_msg:
			tmp_msg.append(x - self.key)
		return tmp_msg

	def translate_ascii(self):
		tmp_msg = []
		for x in self.decoded_ascii_message:
			tmp_msg.append(chr(x))
		return ''.join(tmp_msg)



data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		msg = AsciiDecode( x.strip('\n') )
		print msg



























