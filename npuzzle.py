#/usr/bin/python

import parser

class State():
    def __init__(self, x, y, parent: State):
        self.steps_count = 0
        self.wrong_states_count = 0
        self.x = x
        self.y = y
        self.parent = parent

    def getWeight(self):
        return self.steps_count + self.wrong_states_count

    def getParent(self):
        return self.parent

    def setParent(self, parent: State):
        self.parent = parent

    def setStepsCount(self, steps_count: int):
        self.steps_count = steps_count

    def setWrongStatesCount(self, wrong_states_count: int):
        self.wrong_states_count = wrong_states_count


if __name__ == "__main__":
    puzzle = parser.parse_puzzles
