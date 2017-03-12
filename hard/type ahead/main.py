"""
@Project Name - main
@author - JOHNATHAN
@date - 6/14/2016
@time - 9:03 PM
@url - https://www.codeeval.com/open_challenges/55/
"""

import os
import sys


class Predict():
    def __init__(self, ngrams, word):
        self.ngrams = ngrams
        self.word = word
        self.text = self.feed()
        self.indices = self.indices()

        pass

    def feed(self):
        text = ''
        hard_text = '''Mary had a little lamb its fleece was white as snow;
						And everywhere that Mary went, the lamb was sure to go.
						It followed her to school one day, which was against the rule;
						It made the children laugh and play, to see a lamb at school.
						And so the teacher turned it out, but still it lingered near,
						And waited patiently about till Mary did appear.
						"Why does the lamb love Mary so?" the eager children cry; "Why, Mary loves the lamb, you know" the teacher did reply."
		'''
        for letter in hard_text.replace('\n', ' '):
            if letter.isalpha() or letter == ' ':
                text += letter
        text = text.split(' ')
        return text

    def indices(self):
        self.indices = []
        index = 0
        while True:
            try:
                self.indices.append(self.text.index(self.word, index))
                index = self.indices[-1] + 1
            except ValueError:
                return self.indices

    def previously_used_words(self):
        previous_words = []
        for index in self.indices:
            previous_words.extend(self.text[index + 1:index + self.ngrams])
        return previous_words

    def statistics(self):
        previous_words = self.previously_used_words()
        stats = {}
        for word in set(previous_words):
            try:
                stats[previous_words.count(word) / float(len(previous_words))] += [word]
            except KeyError:
                stats[previous_words.count(word) / float(len(previous_words))] = [word]
        return stats

    def next_words(self):
        stats = self.statistics()
        for item in sorted(stats.keys(), reverse=True):
            if len(stats[item]) > 1:
                stats[item] = sorted(stats[item])  # alphabetical order of similar values

        for item in sorted(stats.keys(), reverse=True):
            if len(stats[item]) == 1:
                sys.stdout.write(stats[item][0] + ',' + '{:.3f}'.format(item))

            if len(stats[item]) > 1:
                for sub_item in stats[item]:
                    sys.stdout.write(str(sub_item) + ',' + '{:.3f}'.format(item))
                    if sub_item != stats[item][-1]:
                        sys.stdout.write(';')
            if item != sorted(stats.keys(), reverse=True)[-1]:
                sys.stdout.write(';')
        sys.stdout.write('\n')


try:
    data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
    with open(data_file, 'r') as input_file:
        data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
    with open(sys.argv[1], 'r') as input_file:
        data = [x.strip('\n') for x in input_file.read().split('\n') if x]

for x in data:
    num, word = x.split(',')
    guess = Predict(int(num), word)
    guess.next_words()
