#/usr/bin/python

from State import *
import functions

class Astar():
    def __init__(self, puzzle_size, is_debug = False):
        self.puzzle_size = puzzle_size
        self.opened = []
        self.closed = []
        self.is_debug = is_debug

    def __str__(self):
        result = "Opened states: ["
        for i in self.opened:
            if self.is_debug:
                result += i.__str__() + "\n"
            else:
                result += str(i.index) + ", "
        result += "]\n"

        result += "Closed states: "
        for i in self.closed:
            if self.is_debug:
                result += i.__str__() + "\n"
            else:
                result += str(i.index) + ", "
        result += "]"

        return result

    def markStateAsClosed(self, state):
        self.closed.append(state)

    def processNeighbors(self, puzzle, state: State):
        curr_index = state.index
        indexes = state.getNeighborIndexes(self.puzzle_size)

        if (self.is_debug):
            print("Neighbors:")
            print(indexes)

        for neighbor in indexes:
            if neighbor in self.closed:
                continue
            
            puzzle_copy = puzzle.copy()
            buf = puzzle_copy[neighbor]
            puzzle_copy[neighbor] = puzzle_copy[curr_index]
            puzzle_copy[curr_index] = buf

            new_state = State(neighbor, state)
            
            new_state.steps_count = state.steps_count + 1
            new_state.heuristic_weight = functions.countHeuristicWeight(puzzle_copy)

            for i in self.opened:
                if new_state.index == i.index and new_state < i:
                    i = new_state
                    continue

            self.opened.append(new_state)
            
        # return None