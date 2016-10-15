"""
@Project Name - poker hands
@author - Johnathan
@date - 1/26/2016
@time - 8:45 PM

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, Ten, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value wins; for example,
	a pair of eights beats a pair of fives. But if two ranks tie, for example, both players have a pair of queens,
 	then highest cards in each hand are compared; if the highest cards tie then
 	the next highest cards are compared, and so on.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains 2 hands (left and right). Cards and hands are separated by space. E.g.

6D 7H AH 7S QC 6H 2D TD JD AS
JH 5D 7H TC JS JD JC TS 5S 7S
2H 8C AD TH 6H QD KD 9H 6S 6C
JS JH 4H 2C 9H QH KC 9D 4D 3S
TC 7H KH 4H JC 7D 9S 3H QS 7S
OUTPUT SAMPLE:

Print out the name of the winning hand or "none" in case the hands are equal. E.g.

left
none
right
left
right

"""

import os
import sys


class ScorePokerHand(object):
	"""

	"""

	def __init__(self, hand, position):
		# self.hand = sorted([int(x) for x in hand], reverse=True)  # Might have to sort the list
		self.hand = self.change_high_card_values(hand)
		self.position = position
		self.card_num_only = sorted([int(x[:-1]) for x in self.hand], reverse=True)
		self.suites_only = [x[-1] for x in self.hand]
		self.is_straight = self.straight()
		self.is_flush = self.flush()
		self.score = self.score_hand(self.hand)


	def __repr__(self):
		return self.hand_name

	def score_hand(self, hand):
		'''

		return value of hand with supplementary score (high card)
		:param hand:
		:return: score
		'''

		if len(set(self.card_num_only)) == 4:
			#  Hand contains 1 pair
			pairs = set([int(x) for x in self.card_num_only if self.card_num_only.count(x) == 2])
			self.hand_value = list(pairs)
			self.hand_name = 'One Pair'
			self.high_cards = [int(x) for x in self.card_num_only if self.card_num_only.count(x) == 1]
			return 1

		if len(set(self.card_num_only)) == 3 and len(set([x for x in self.card_num_only if self.card_num_only.count(x) == 2])) == 2:
			#  Hand contains 2 pair
			pairs = set([int(x) for x in self.card_num_only if self.card_num_only.count(x) == 2])
			self.hand_value = list(pairs)
			self.score = 2
			self.hand_name = 'Two Pair'
			self.high_cards = [int(x) for x in self.card_num_only if self.card_num_only.count(x) == 1]
			return 2

		if len(set(self.card_num_only)) == 3 and len(set([x for x in self.card_num_only if self.card_num_only.count(x) == 3])) == 1:
			#  Hand contains 3 of a kind
			pairs = set([int(x) for x in self.card_num_only if self.card_num_only.count(x) == 3])
			self.hand_value = list(pairs)
			self.score = 3
			self.hand_name = 'Three of a Kind'
			self.high_cards = [int(x) for x in self.card_num_only if self.card_num_only.count(x) == 1]
			return 3

		if self.is_straight and not self.is_flush:
			#  Hand contains a straight
			self.score = 4
			self.hand_name = 'Straight'
			self.hand_value = self.card_num_only
			return 4

		if self.is_flush and not self.is_straight:
			#  Hand contains a flush
			self.score = 5
			self.hand_name = 'Flush'
			self.hand_value = self.card_num_only
			return 5

		if len(set(self.card_num_only)) == 2 and \
						len(set([x for x in self.card_num_only if self.card_num_only.count(x) == 3])) == 1 and \
						len(set([x for x in self.card_num_only if self.card_num_only.count(x) == 2])) == 1:
			#  Hand contains a full house
			pairs = set([x for x in self.card_num_only if self.card_num_only.count(x) == 3])
			pairs = list(pairs)
			pairs.append(list(set([x for x in self.card_num_only if self.card_num_only.count(x) == 2]))[0])
			self.hand_value = pairs
			self.score = 6
			self.hand_name = 'Full House'
			self.high_cards = [int(x) for x in self.card_num_only if self.card_num_only.count(x) == 1]
			return 6

		if len(set(self.card_num_only)) == 2 and len(set([x for x in self.card_num_only if self.card_num_only.count(x) == 4])) == 1:
			#  Hand contains a four of a kind
			pairs = set([x for x in self.card_num_only if self.card_num_only.count(x) == 4])
			self.hand_value = list(pairs)
			self.score = 7
			self.hand_name = 'Four of a kind'
			self.high_cards = [int(x) for x in self.card_num_only if self.card_num_only.count(x) == 1]
			return 7

		if self.is_straight and self.is_flush and self.card_num_only != [14,13,12,11,10]:
			#  Hand contains straight flush
			if self.card_num_only == [14, 5, 4, 3, 2]:
				self.card_num_only.remove(14)
				self.card_num_only.append(1)
			self.score = 8
			self.hand_name = 'Straight Flush'
			self.hand_value = self.card_num_only
			return 8

		if self.is_straight and self.is_flush and self.card_num_only == [14,13,12,11,10]:
			#  Hand contains royal flush
			self.score = 9
			self.hand_name = 'Royal Flush'
			self.hand_value = self.card_num_only
			return 9
		else:
			#  Hand only contains high card
			self.score=0
			self.hand_name = 'High Card'
			self.hand_value = self.card_num_only
			return 0


	def straight(self):
		card = int(self.card_num_only[0])
		if self.card_num_only == [14, 5, 4, 3, 2]:
			return True
		for x in self.card_num_only[1:]:
			if int(x) != card - 1:
				return False
			card = int(x)
		return True

	def flush(self):
		if len(set(self.suites_only)) == 1:
			return True
		return False

	def change_high_card_values(self, unclean_hand):
		'''
		return high cards as values instead of strings
		:param hand: list of cards
		:return:  list of cards with high cards returned as values
		'''
		new_hand = []
		for x in unclean_hand:
			if x[0] == 'T':
				new_hand.append('10' + x[-1])
			elif x[0] == 'J':
				new_hand.append('11' + x[-1])
			elif x[0] == 'Q':
				new_hand.append('12' + x[-1])
			elif x[0] == 'K':
				new_hand.append('13' + x[-1])
			elif x[0] == 'A':
				new_hand.append('14' + x[-1])
			else:
				new_hand.append(x)
		return new_hand


def winner_by_hand_value(hand_value1, hand_value2):
	for x in xrange(len(hand_value1.hand_value)):
		if hand_value1.hand_value[x] > hand_value2.hand_value[x]:
			return hand_value1
		if hand_value1.hand_value[x] < hand_value2.hand_value[x]:
			return hand_value2
	# hand values are the same need to evaluate high cards if any
	try:
		winner_by_high_card(hand_value1, hand_value2)
	except AttributeError:
		# unless there are no high cards, in the case of hand_name == High Card
		return 'None'

def winner_by_high_card(hand_value1, hand_value2):
	for x in xrange(len(hand_value1.high_card)):
		if hand_value1.high_card[x] > hand_value2.high_card[x]:
			return hand_value1
		if hand_value1.high_card[x] < hand_value2.high_card[x]:
			return hand_value2
	return None

def winner_by_score(hand_value1, hand_value2):
	if hand_value1.score > hand_value2.score:
		return hand_value1
	elif hand_value1.score < hand_value2.score:
		return hand_value2
	# contain the same hand need to evaluate hand value
	return winner_by_hand_value(hand_value1, hand_value2)




data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
	for x in input_file.readlines():
		x_list = x.split()
		left_hand = x[:len(x) / 2].split()
		right_hand = x[len(x) / 2:].split()

		left_hand = ScorePokerHand(left_hand, 'left')
		right_hand = ScorePokerHand(right_hand, 'right')


		winner = winner_by_score(left_hand, right_hand)


		'''print " Winner: {0} | Left hand: {1}  Right Hand: {2}".format(
																winner.position if hasattr(winner, 'position') else 'none',
																left_hand.hand,
																right_hand.hand)'''
		sys.stdout.write(winner.position + '\n' if hasattr(winner, 'position') else 'none\n')


