#/usr/bin/python

from Functions import *
from State import *

class Astar():
    def __init__(self, func: Functions, is_debug = False):
        self.opened = []
        self.closed = []
        self.func     = func
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
        # for i in range(0, 40):
        while (self.opened):
            next_state = min(self.opened)

            if self.func.isFinished(next_state.puzzle.map):
                self.func.printFullPath(next_state)
                print("FIIIIINNIIIISH ")
                break
        
            self.opened.remove(next_state)
            self.closed.append(next_state)
            self.processNeighbors(next_state)

            if self.is_debug:
                print("Next State:")
                print(next_state)
                print("Opened:")
                self.func.printStateList(self.opened)
                print("Closed:")
                self.func.printStateList(self.closed)

            # current_state = next_state
            
            # if is_debug:
            #     print(puzzle)


    def processNeighbors(self, state: State):
        neighbors = state.getNeighborStates()

        for neighbor in neighbors:
            # print(neighbor.puzzle.index)
            if neighbor in self.closed:
                continue
            
            neighbor.steps_count = state.steps_count + 1
            neighbor.heuristic_weight = self.func.countHeuristicWeight(neighbor.puzzle.map)

            is_already_opened = False

            for i in self.opened:
                if neighbor == i and neighbor.steps_count < i.steps_count:
                    i.parent = state
                    i.steps_count = neighbor.steps_count
                    is_already_opened = True
                    if self.is_debug:
                        print("\nAlready opened:\n")
                        print(i)
                    break

            if is_already_opened:
                continue

            self.opened.append(neighbor)

        # return None