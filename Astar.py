#/usr/bin/python

from State import *
import functions

class Astar():
    def __init__(self, is_debug = False):
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

    def processNeighbors(self, state: State):
        neighbors = state.getNeighborStates()

        if (self.is_debug):
            print("Neighbors:")
            string = ""
            for i in neighbors:
                string += str(i.puzzle.index) + ", "
            print(string)

        for neighbor in neighbors:
            if neighbor in self.closed:
                continue
            
            neighbor.steps_count = state.steps_count + 1
            neighbor.heuristic_weight = functions.countHeuristicWeight(neighbor.puzzle.map)

            # for i in self.opened:
            #     if neighbor == i and new_state < i:
            #         i = new_state
            #         continue

            self.opened.append(neighbor)
            
        # return None