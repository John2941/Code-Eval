"""
@Project Name - computer terminal hard
@author - Johnathan
@date - 3/12/2016
@time - 1:53 PM
@url - https://www.codeeval.com/open_challenges/108/

^c - clear the entire screen; the cursor row and column do not change
^h - move the cursor to row 0, column 0; the image on the screen is not changed
^b - move the cursor to the beginning of the current line; the cursor row does not change
^d - move the cursor down one row if possible; the cursor column does not change
^u - move the cursor up one row, if possible; the cursor column does not change
^l - move the cursor left one column, if possible; the cursor row does not change
^r - move the cursor right one column, if possible; the cursor row does not change
^e - erase characters to the right of, and including, the cursor column on the cursor's row; the cursor row and column do not change
^i - enter insert mode
^o - enter overwrite mode
^^ - write a circumflex (^) at the current cursor location, exactly as if it was not a special character; this is subject to the actions of the current mode (insert or overwrite)
^DD - move the cursor to the row and column specified; each D represents a decimal digit; the first D represents the new row number, and the second D represents the new column number
"""
import sys
import os

class terminal():
    def __init__(self, raw_actions=""):
        self.row = 10
        self.column = 10
        self.cursor = [0,0]  # (column, row)
        self.display = self.initialize_display()
        self.insert_mode = True
        self.overwrite_mode = False
        self.verbose = False

    def initialize_display(self):
        list_obj = list()
        for x in range(self.row):
            list_obj.append([" "] * self.column)
        return list_obj


    def parse_actions(self):
        if not hasattr(self, 'raw_actions'):
            print "You need to give raw_actions"
        prev_circumflex = False
        expect_next_digit = None
        prev_circumflex_escape = False
        for x in self.raw_actions:
            command_character = False
            if prev_circumflex:
                prev_circumflex = False
                if x == "^":
                    # means the circumflex is suppose to be the printed char
                    prev_circumflex_escape = True
                if x.isdigit():
                    expect_next_digit = x  # cmds with digits requires two ints
                    continue
                if x.isalpha():
                    cmd = x
                    command_character = True
            if expect_next_digit:
                if x.isdigit():
                    cmd = expect_next_digit + x
                    command_character = True
            if x == "^" and not prev_circumflex_escape:
                prev_circumflex = True  # parse the character following the circumflex
                continue
            prev_circumflex_escape = False
            if expect_next_digit:
                expect_next_digit = None
            else:
                cmd = x
            self.determine_action(cmd, command_character)


    def determine_action(self, str_cmd, command_character):
        """
        :param str_cmd: the cmd or normal character
        :param command_character: boolean; True if str_cmd is part of a cmd
        :return:
        """
        if command_character:
            if len(str_cmd) == 2 and str_cmd.isdigit():
                if self.verbose: print "Moving cursor to " + str_cmd[0] + ',' + str_cmd[1] + ".",
                self.cursor = [int(str_cmd[1]),int(str_cmd[0])]
            elif str_cmd == 'c':
                if self.verbose: print "Clearing screen.",
                self.display = self.initialize_display()
            elif str_cmd == 'h':
                if self.verbose: print "Resetting cursor to 0,0.",
                self.cursor = [0,0]
            elif str_cmd == 'b':
                if self.verbose: print "Resetting cursor column to 0.",
                self.cursor[0] = 0
            elif str_cmd == 'i':
                if self.verbose: print "Entering insert mode.",
                self.insert_mode = True
                self.overwrite_mode = False
            elif str_cmd == 'o':
                if self.verbose: print "Entering overwrite mode.",
                self.insert_mode = False
                self.overwrite_mode = True
            elif str_cmd == 'd':
                if self.verbose: print "Move cursor down one.",
                if self.cursor[1] + 1 < self.row:
                    self.cursor[1] += 1
            elif str_cmd == 'u':
                if self.verbose: print "Move cursor up one.",
                if self.cursor[1] - 1 >= 0:
                    self.cursor[1] -= 1
            elif str_cmd == 'r':
                if self.verbose: print "Move cursor right one.",
                if self.cursor[0] + 1 < self.column:
                    self.cursor[0] += 1
            elif str_cmd == 'l':
                if self.verbose: print "Move cursor left one.",
                if self.cursor[0] - 1 >= 0:
                    self.cursor[0] -= 1
            elif str_cmd == 'e':
                if self.verbose: print "Erasing everything to the right.",
                for x in xrange(self.column - self.cursor[0]):
                    self.display[self.cursor[1]].insert(self.cursor[0], '*')
                self.display[self.cursor[1]] = self.display[self.cursor[1]][:self.column]
        else:
            if self.overwrite_mode:
                self.display[self.cursor[1]][self.cursor[0]] = str_cmd
            if self.insert_mode:
                self.display[self.cursor[1]].insert(self.cursor[0], str_cmd)
                self.display[self.cursor[1]] = self.display[self.cursor[1]][:self.column]
                # Have to remove the extra characters that were pushed forward pas the column limit
            if self.verbose: print "Adding " + str_cmd + ".",
            self.move_cursor(col=1)
        if self.verbose: print " Cursor location: " + ",".join(str(x) for x in self.cursor)
        if self.verbose: term.print_term()

    def move_cursor(self, set_col=None, set_row=None, col=None, row=None):
        """
        :param col: move column by this much; default will move cursor 1 to the right
        :param row: move row by this much
        :return:
        """
        if set_col != None:
            if 0 <= set_col < self.column:
                self.cursor[0] = set_col
        if set_row != None:
             if 0 <= set_row < self.row:
                self.cursor[1] = set_row
        if col != None:
            if col > 0:
                if self.cursor[0] + col < self.column:
                    self.cursor[0] += col
            if col < 0:
                if self.cursor[0] - col >= 0:
                    self.cursor[0] -= col
        if row != None:
            if row > 0:
                if self.cursor[1] + row < self.row:
                    self.cursor[1] += row
            if row < 0:
                if self.cursor[1] - row >= 0:
                    self.cursor[1] -= row
    def print_term(self):
        for x in self.display:
            print "".join(x)



term = terminal()
data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

# with open(sys.argv[1],'r') as input_file:
with open(data_file, 'r') as input_file:
    for x in input_file.readlines():
        x = x.strip('\n')
        term.raw_actions = x
        term.parse_actions()
term.print_term()
