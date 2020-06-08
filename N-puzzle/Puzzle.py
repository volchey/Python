#/usr/bin/python

class Puzzle():
    def __init__(self, map: tuple, size: int):
        self.map = map
        self.size = size
        self.index = self.map.index(0)
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

    def getMovedToIndex(self, a_index: int):
        new_list = list(self.map)
        new_list[a_index] = self.map[self.index]
        new_list[self.index] = self.map[a_index]

        return Puzzle(tuple(new_list), self.size)