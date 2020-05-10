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
            is_in_closed = False
            for close in self.closed:
                if close.puzzle.hash == neighbor.puzzle.hash:
                    is_in_closed = True
                    break

            if is_in_closed:
                continue

            neighbor.steps_count = state.steps_count + 1

            is_already_opened = False

            for i in self.opened:
                if neighbor.puzzle.hash == i.puzzle.hash:
                    is_already_opened = True
                    if neighbor.steps_count < i.steps_count:
                        i.parent = state
                        i.steps_count = neighbor.steps_count
                    break

            if is_already_opened:
                continue

            neighbor.countHeuristicWeight()
            self.markAsOpened(neighbor)
            # self.opened.append(neighbor)