#/usr/bin/python

import State

class Functions():
    def __init__(self, map_size, is_debug = False):
        self.map_size = map_size
        self.is_debug = is_debug
        self.goal     = self.findGoalState()
        
    def findGoalState(self):
        map_size = self.map_size
        goal = []
        for i in range(0, map_size):
            new = [0] * map_size
            goal.append(new)
        
        x = -1
        y = 0 
        value = 0
        max_value = map_size * map_size
        while value < max_value - 1:
            for i in range(0, map_size):
                x += 1
                value += 1
                goal[y][x] = value
            map_size -=1
            for i in range(0, map_size):
                y += 1
                value += 1
                goal[y][x] = value
            for i in range(0, map_size):
                x -= 1
                value += 1
                if (value == max_value):
                    break
                goal[y][x] = value
            map_size -= 1
            for i in range(0, map_size):
                y -= 1
                value += 1
                if (value == max_value):
                    break
                goal[y][x] = value
        
        if self.is_debug:
            print("Goal:")
            for i in goal:
                print(i)

        result = []
        for y in goal:
            for x in y:
                result.append(x)

        return result
            
    def countHeuristicWeight(self, puzzle):
        result = 0
        for index, value in enumerate(puzzle):
            if self.goal[index] != value:
                result += 1
        return result

    # def heuristic(self, state):
    #     x, y = state.puzzle.getIndexCoords(state.puzzle.index)
    #     dx = abs(x - goal.x)
    #     dy = abs(y - goal.y)
    #     return (dx + dy)

    def isFinished(self, puzzle):
        return self.countHeuristicWeight(puzzle) == 0

    def printStateList(self, list):
        string = ""
        for i in list:
            string += str(i.puzzle.index) + ", "
        print(string)

    def printFullPath(self, state: State):
        while True:
            print(state)
            if not state.parent:
                break
            print("^")
            print("|")
            state = state.parent
