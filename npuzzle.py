#/usr/bin/python

import parser
import functions
from Astar import *
from State import *
from Puzzle import *

is_debug = True

def isFinished(puzzle):
    return functions.countHeuristicWeight(puzzle) == 1

if __name__ == "__main__":
    map, map_size = parser.parse_puzzles()

    puzzle = Puzzle(map, map_size)

    current_state = State(puzzle, None)

    # if (current_state == None):
    #     print("invalid puzzle - no start found")
    #     exit(2)
        
    if is_debug:
        print ("Puzzle start:")
        print(current_state)

    astar = Astar(is_debug)
    astar.opened.append(current_state)

    if is_debug:
        print(puzzle)
        
    # for i in range(0, 40):
    while (astar.opened):
        next_state = min(astar.opened)

        if isFinished(next_state.puzzle.map):
            break
    
        astar.opened.remove(next_state)
        astar.closed.append(next_state)
        astar.processNeighbors(next_state)

        if is_debug:
            print("Next State:")
            print(next_state)

        # current_state = next_state
        
        # if is_debug:
        #     print(puzzle)

