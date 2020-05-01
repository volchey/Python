#/usr/bin/python

import parser
from Functions import *
from Astar import *
from State import *
from Puzzle import *

is_debug = False

if __name__ == "__main__":
    try:
        map, map_size = parser.parse_puzzles()
    except Exception as e:
        print(e)
        exit(2)

    func = Functions(map_size, is_debug)
    puzzle = Puzzle(map, map_size)

    current_state = State(puzzle, None)

    astar = Astar(func, is_debug)
    astar.opened.append(current_state)
    astar.search()
