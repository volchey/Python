#/usr/bin/python

from heapq import heappush, heappop, heapify
from State import *

class Astar():
    def __init__(self, is_debug = False):
        self.opened = []
        heapify(self.opened)
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

    def markAsOpened(self, state: State):
        heappush(self.opened, state)
        # self.opened.append(state)

    def getMinFromOpened(self):
        # state = min(self.opened)
        # self.opened.remove(state)
        # return state
        return heappop(self.opened)

    def search(self):
        while (self.opened):
            next_state = self.getMinFromOpened()

            if next_state.isFinished():
                next_state.printFullPath()
                print("FIIIIINNIIIISH ")
                break

            self.closed.append(next_state)
            self.processNeighbors(next_state)

            if self.is_debug:
                print("Next State:")
                print(next_state)


    def processNeighbors(self, state: State):
        neighbors = state.getNeighborStates()

        for neighbor in neighbors:
            if neighbor in self.closed:
                continue

            neighbor.steps_count = state.steps_count + 1

            if neighbor in self.opened:
                i = self.opened.index(neighbor)
                elem = self.opened[i]
                if neighbor.steps_count < elem.steps_count:
                    elem.parent = state
                    elem.steps_count = neighbor.steps_count
                continue

            neighbor.countHeuristicWeight()
            self.markAsOpened(neighbor)
            # self.opened.append(neighbor)