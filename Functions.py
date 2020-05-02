#/usr/bin/python

class Functions():
    def __init__(self, map_size, is_debug = False):
        self.map_size   = map_size
        self.max_value  = self.map_size * self.map_size
        self.is_debug   = is_debug
        self.goal       = self.findGoalState()
        self.map_coords = self.findMapCoords()
        self.goal_hash  = hash(tuple(self.goal))
        
    def findGoalState(self):
        map_size = self.map_size
        goal = []
        for i in range(0, map_size):
            new = [0] * map_size
            goal.append(new)
        
        x = -1
        y = 0 
        value = 0
        while value < self.max_value - 1:
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
                if (value == self.max_value):
                    break
                goal[y][x] = value
            map_size -= 1
            for i in range(0, map_size):
                y -= 1
                value += 1
                if (value == self.max_value):
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
            
    def findMapCoords(self):
        result = {}
        x = 0
        y = 0
        for i in range(self.max_value):
            result[i] = (x, y)
            x += 1
            if x % self.map_size == 0:
                x = 0
                y += 1
            
        return result

    def printStateList(self, list):
        string = ""
        for i in list:
            string += str(i.puzzle.index) + ", "
        print(string)

    def getIndexCoords(self, index: int):
        if index < 0 or index > (self.max_value - 1):
            return (-1, -1)

        return self.map_coords[index]

    def getValueCoords(self, a_value: int):
        if a_value < 0 or a_value > (self.max_value - 1):
            return (-1, -1)

        for index, value in enumerate(self.goal):
            if value == a_value:
                return self.map_coords[index]

        return (-1, -1)