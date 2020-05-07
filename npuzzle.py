#/usr/bin/python
import time
import sys
from Parser import *
from Functions import *
from Astar import *
from State import *
from Puzzle import *

is_debug = False

if __name__ == "__main__":
    st = time.time()

    if "-d" in sys.argv:
        is_debug = True
    
    try:
        parser = Parser(is_debug)
        map, map_size = parser.parse_puzzles()
    except Exception as e:
        print(e)
        exit(2)

    func = Functions(map_size, is_debug)
    puzzle = Puzzle(map, map_size)

    current_state = State(func, puzzle, None)

    astar = Astar(is_debug)
    astar.opened.append(current_state)
    astar.search()

    print("----%.2f----" % (time.time() - st))
