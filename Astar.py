#/usr/bin/python

from State import *

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

    def search(self):
        # for i in range(0, 20):
        while (self.opened):
            next_state = min(self.opened)

            if next_state.isFinished():
                next_state.printFullPath()
                print("FIIIIINNIIIISH ")
                break

            self.opened.remove(next_state)
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

            if neighbor not in self.opened:
                neighbor.countHeuristicWeight()
                self.opened.append(neighbor)
                continue

            for i in self.opened:
                if neighbor == i and neighbor.steps_count < i.steps_count:
                    i.parent = state
                    i.steps_count = neighbor.steps_count
                    is_already_opened = True
                    break
