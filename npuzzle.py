#/usr/bin/python

import parser
import functions
from Astar import *
from State import *

is_debug = True

def findStart(puzzle):
    for index, value in enumerate(puzzle):
        if (value == 0):
            return State(index, None, is_debug)

    return None

def isFinished(puzzle):
    return functions.countHeuristicWeight(puzzle) == 0

def printPuzzle(puzzle, puzzle_size):
    result = ""
    for index, value in enumerate(puzzle):
        result += str(value) + " | "
        if index + 1 % puzzle_size == 0:
            result += "\n"

    print(result)

if __name__ == "__main__":
    puzzle, puzzle_size = parser.parse_puzzles()

    current_state = findStart(puzzle)

    if (current_state == None):
        print("invalid puzzle - no start found")
        exit(2)
        
    # if is_debug:
    #     print ("Puzzle start:")
    #     print(current_state)

    astar = Astar(puzzle_size, is_debug)
    astar.markStateAsClosed(current_state)
    astar.processNeighbors(puzzle, current_state)

    if is_debug:
        print(astar)
    
    while (astar.opened and not isFinished(puzzle)):
        next_state = min(astar.opened)
    
        if is_debug:
            print("Next State:")
            print(next_state)
        
        buf = puzzle[next_state.index]
        puzzle[next_state.index] = puzzle[current_state.index]
        puzzle[current_state.index] = buf
        current_state = next_state
        astar.markStateAsClosed(current_state)
        astar.processNeighbors(puzzle, current_state)

        astar.opened.remove(next_state)
    
    printPuzzle(puzzle, puzzle_size)

