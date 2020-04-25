#/usr/bin/python

from Puzzle import *

class State():
    def __init__(self, puzzle: Puzzle, parent, is_debug = False):
        self.puzzle = puzzle
        self.steps_count = 0
        self.heuristic_weight = 0
        self.parent = parent
        self.is_debug = is_debug

    def __str__(self):
        return "Puzzle:\n{}Steps count (g) = {}\nHeuristic weight (h) = {}".format(
            self.puzzle.__str__(), self.steps_count, self.heuristic_weight)

    def __eq__(self, other):
        # if (other == None):
        #     return False
        print("Equal operator called")
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return self.getWeight() < other.getWeight()

    def __gt__(self, other):
        return self.getWeight() > other.getWeight()

    def createNewStateFromIndex(self, index):
        map_copy = self.puzzle.map.copy()
        buf = map_copy[index]
        map_copy[index] = map_copy[self.puzzle.index]
        map_copy[self.puzzle.index] = buf
        return State(Puzzle(map_copy, self.puzzle.size), self, self.is_debug)

    def getNeighborStates(self):
        index = self.puzzle.index
        curr_col, curr_row = self.puzzle.getIndexCoords(index)
        states = []
        
        left = index - 1
        left_col, left_row = self.puzzle.getIndexCoords(left)
        # print("left_column = {}, left_row = {}".format(left_col, left_row))
        if (left_row == curr_row and left_col >= 0):
            states.append(self.createNewStateFromIndex(left))
        
        right = index + 1
        right_col, right_row = self.puzzle.getIndexCoords(right)
        if (right_row == curr_row and right_col <= self.puzzle.size - 1):
            states.append(self.createNewStateFromIndex(right))

        up = index - self.puzzle.size
        up_col, up_row = self.puzzle.getIndexCoords(up)
        if (up_col == curr_col and up_row >= 0):
            states.append(self.createNewStateFromIndex(up))
        
        down = index + self.puzzle.size
        down_col, down_row = self.puzzle.getIndexCoords(down)
        if (down_col == curr_col and down_row <= self.puzzle.size - 1):
            states.append(self.createNewStateFromIndex(down))
        
        return states

    def getWeight(self):
        return self.steps_count + self.heuristic_weight


