#/usr/bin/python

class Puzzle():
    def __init__(self, map: tuple, size: int):
        self.map = map
        self.size = size
        self.index = self.getIndex()
        self.hash = hash(map)

    def __str__(self):
        result = ""
        for index, value in enumerate(self.map):
            result += str(value) + " | "
            if (index + 1) % self.size == 0:
                result += "\n"

        return result

    def __eq__(self, value):
        return self.hash == value.hash

    def getIndex(self) -> int:
        for index, value in enumerate(self.map):
            if (value == 0):
                return index
        return None

    def getMovedToIndex(self, a_index: int):
        new_list = []
        for i, value in enumerate(self.map):
            if i == a_index:
                value = 0
            elif i == self.index:
                value = self.map[a_index]
            new_list.append(value)
        
        # map_copy = self.map
        # buf = map_copy[index]
        # map_copy[index] = map_copy.index(self.index)
        # map_copy[self.index] = buf
        return Puzzle(tuple(new_list), self.size)