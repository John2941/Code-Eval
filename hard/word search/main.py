"""
@Project Name - main
@author - Johnathan
@date - 10/14/2016
@time - 5:14 PM

"""
import os
import sys

try:
    data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"
    with open(data_file, 'r') as input_file:
        data = [x.strip('\n') for x in input_file.read().split('\n') if x]
except IOError:
    with open(sys.argv[1], 'r') as input_file:
        data = [x.strip('\n') for x in input_file.read().split('\n') if x]

class WordSearch():
    def __init__(self):
        self.board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.used_cells = []
        self.current_position = False
        self.letters_processed = ''
        self.starting_indexes = []
        self.location_cache = {}


    def initialize_search(self, letter_to_find):
        # If current_position has not been set, then we need to find all occurrences
        #   of the first letter to initialize the search
        for row_index, row in enumerate(self.board):
            for letter_index, letter in enumerate(row):
                if letter == letter_to_find:
                    self.starting_indexes.append([row_index, letter_index])
        if len(self.starting_indexes) == 0:
            return False
        self.current_position = self.starting_indexes[0]
        self.update_location_cache(letter_to_find, self.current_position, 0)
        self.used_cells.append(self.current_position)
        return True

    def catch_up(self, starting_letter):
        for letter_index, letter in enumerate(self.letters_processed + starting_letter):
            if not self.next_letter(letter, letter_index + 1):
                return False
        return True

    def next_letter(self, letter_to_find, letter_index):
        # Must attempt to move all four possible moves (down, up, right, and left)
        letter_found = False
        if not self.current_position:
            return self.initialize_search(letter_to_find)
        possible_moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for move in possible_moves:
            l = self.get_index(move)
            if l['letter'] == letter_to_find:
                if not letter_found:
                    self.used_cells.append(l['index'])
                    self.letters_processed += l['letter']
                    letter_found = True
                self.update_location_cache(l['letter'], l['index'], letter_index)
        if letter_found:
            self.current_position = self.used_cells[-1]
            return True
        else:
            next_trail = self.is_there_another_path()
            if next_trail:
                # Check here for any letters that were found twice
                #   then go back and check those trails
                self.location_cache[next_trail]['location'] = self.location_cache[next_trail]['location'][1:]
                # Erase the old position that couldn't find the next letter
                self.current_position = self.location_cache[next_trail]['location'][0]
                # Set current position to the earliest letter where more than 1 letter was found
                self.used_cells = self.used_cells[:next_trail]
                self.used_cells.append(self.current_position)
                catch_up_letters = self.letters_processed[next_trail:]
                self.letters_processed = self.letters_processed[:next_trail]
                # need to pass the remaining letters to a next_letter loop to catch up to where the main loop is at
                if not catch_up_letters:
                    catch_up_letters = letter_to_find
                for letter_index, letter in enumerate(catch_up_letters):
                    if not self.next_letter(letter, len(self.letters_processed) + letter_index + 1):
                        return False
                    return True

        if self.starting_indexes[1:]:
            # Clear previous histories and start with the next first letter originally found
            self.starting_indexes = self.starting_indexes[1:]
            self.current_position = self.starting_indexes[0]
            first_letter = self.board[self.current_position[0]][self.current_position[1]]
            self.update_location_cache(
                                        first_letter,
                                        self.current_position,
                                        0,
                                        erase=True
            )
            self.used_cells = [self.current_position]
            if self.catch_up(letter_to_find):
                return True
        return letter_found

    def is_there_another_path(self):
        for index in self.location_cache:
            if len(self.location_cache[index]['location']) > 1:
                return index
        return False

    def update_location_cache(self, letter, location, index, erase=False):
        if erase:
            self.location_cache = {
                                    index: {
                                        'letter': letter,
                                        'location': [location]
                                    }
            }
            return
        if index in self.location_cache.keys():
            self.location_cache[index]['location'].append(location)
        else:
            self.location_cache[index] = {
                                            'letter': letter,
                                            'location': [location]
            }

    def get_index(self, index_to_move):
        move_index = self.add_indexes(self.current_position, index_to_move)
        if -1 in move_index:
            return {
                'letter': False,
                'index': move_index
            }
        if move_index not in self.used_cells:
            try:
                return {
                    'letter': self.board[move_index[0]][move_index[1]],
                    'index': move_index
                }
            except IndexError:
                pass
        return {
            'letter': False,
            'index': move_index
        }

    def add_indexes(self, first_index, second_index):
        if len(first_index) != 2 or len(second_index) != 2:
            raise Exception("Error attempting to add two indexes of incorrect lengths.")
        return [
            first_index[0] + second_index[0],
            first_index[1] + second_index[1]
        ]

for word in data:
    search = WordSearch()
    found = False
    for letter_index, letter in enumerate(word):
        if not search.next_letter(letter, letter_index):
            break
    else:
        found = True
    print found
