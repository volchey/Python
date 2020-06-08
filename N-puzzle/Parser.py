#/usr/bin/python

import sys

class Parser():
    def __init__(self, is_debug = False):
        self.is_debug = is_debug

    def is_comment(self, line):
        return line[0] == '#'

    def get_puzzle_size(self, file):
        for line in file:
            if self.is_comment(line):
                continue

            size = int(line)
            if (self.is_debug):
                print('{} = {}'.format('puzzle size', size))
            return size
        return 0

    def parse_map(self, puzzle_size, file):
        puzzle = ()

        for line in file:
            if self.is_comment(line):
                continue

            row = line.split()
            row_int = []
            print(row)
            for elem in row:
                if self.is_comment(elem):
                    continue
                row_int.append(int(elem))

            if (len(row) != puzzle_size):
                print('{}: {}'.format("incorrect puzzle map in row", line))
                exit(2)

            puzzle += tuple(row_int)

        return puzzle

    def parse_puzzles(self):
        if len(sys.argv) < 2:
            print("parser.py [filename]")
            exit(2)

        try:
            file=open(sys.argv[1], "r")
        except Exception as a:
            raise a
        
        puzzle_size = self.get_puzzle_size(file)

        if (puzzle_size <= 0):
            print("incorrect puzzle size: {}".format(puzzle_size))
            exit(2)

        puzzle = self.parse_map(puzzle_size, file)

        return puzzle, puzzle_size
    