#/usr/bin/python

import functions

class State():
    def __init__(self, index, parent, is_debug = False):
        self.index = index
        self.steps_count = 0
        self.heuristic_weight = 0
        self.parent = parent
        self.is_debug = is_debug

    def __str__(self):
        return "Index = {}\nSteps count (g) = {}\nHeuristic weight (h) = {}".format(
            self.index, self.steps_count, self.heuristic_weight)

    def __lt__(self, other):
        return self.getWeight() < other.getWeight()

    def __gt__(self, other):
        return self.getWeight() > other.getWeight()

    def getNeighborIndexes(self, puzzle_size):
        curr_col, curr_row = functions.getIndexCoords(self.index, puzzle_size)
        indexes = []
        
        left = self.index - 1
        left_col, left_row = functions.getIndexCoords(left, puzzle_size)
        print("left_column = {}, left_row = {}".format(left_col, left_row))
        if (left_row == curr_row and left_col >= 0):
            indexes.append(left)
        
        right = self.index + 1
        right_col, right_row = functions.getIndexCoords(right, puzzle_size)
        if (right_row == curr_row and right_col <= puzzle_size - 1):
            indexes.append(right)

        up = self.index - puzzle_size
        up_col, up_row = functions.getIndexCoords(up, puzzle_size)
        if (up_col == curr_col and up_row >= 0):
            indexes.append(up)
        
        down = self.index + puzzle_size
        down_col, down_row = functions.getIndexCoords(down, puzzle_size)
        if (down_col == curr_col and down_row <= puzzle_size - 1):
            indexes.append(down)
        
        return indexes

    def getWeight(self):
        return self.steps_count + self.heuristic_weight

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def setStepsCount(self, steps_count):
        self.steps_count = steps_count

    def setWrongStatesCount(self, wrong_states_count):
        self.wrong_states_count = wrong_states_count

