#/usr/bin/python

import math
from Functions import *
from Puzzle import *

class State():
    def __init__(self, func: Functions, puzzle: Puzzle, parent, is_debug = False):
        self.func               = func
        self.puzzle             = puzzle
        self.parent             = parent
        self.is_debug           = is_debug
        self.steps_count        = 0
        self.heuristic_weight   = 0

    def __str__(self):
        return "Puzzle:\n{}Steps count (g) = {}\nHeuristic weight (h) = {}".format(
            self.puzzle.__str__(), self.steps_count, self.heuristic_weight)

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return self.getWeight() < other.getWeight()

    def createNewStateFromIndex(self, index):
        new_puzzle = self.puzzle.getMovedToIndex(index)
        return State(self.func, new_puzzle, self, self.is_debug)

    def getNeighborStates(self):
        index = self.puzzle.index
        curr_col, curr_row = self.func.getIndexCoords(index)
        states = []

        if (curr_col - 1 >= 0):
            states.append(self.createNewStateFromIndex(index - 1))

        if (curr_col + 1 <= self.puzzle.size - 1):
            states.append(self.createNewStateFromIndex(index + 1))

        if (curr_row - 1 >= 0):
            states.append(self.createNewStateFromIndex(index - self.puzzle.size))

        if (curr_row + 1 <= self.puzzle.size - 1):
            states.append(self.createNewStateFromIndex(index + self.puzzle.size))

        return states

    def countHeuristicWeight(self):
        self.heuristic_weight = self.manhattanDistance()

    def missedCount(self):
        result = 0
        for index, value in enumerate(self.puzzle.map):
            if self.func.goal[index] != value:
                result += 1
        return result

    def manhattanDistance(self):
        result = 0
        for index, value in enumerate(self.puzzle.map):
            x, y            = self.func.getIndexCoords(index)
            goal_x, goal_y  = self.func.getValueCoords(value)
            dx = abs(x - goal_x)
            dy = abs(y - goal_y)
            result += dx + dy
        return result

    def euclidianDistance(self):
        result = 0
        for index, value in enumerate(self.puzzle.map):
            x, y            = self.func.getIndexCoords(index)
            goal_x, goal_y  = self.func.getValueCoords(value)
            dx = abs(x - goal_x)
            dy = abs(y - goal_y)
            result += math.sqrt(dx * dx + dy * dy)
        return result

    def getWeight(self):
        return self.steps_count + self.heuristic_weight

    def isFinished(self):
        return self.func.goal_hash == self.puzzle.hash

    def printFullPath(self):
        while True:
            print(self)
            if not self.parent:
                break
            print("^")
            print("|")
            self = self.parent


