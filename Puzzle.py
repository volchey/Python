#/usr/bin/python

class Puzzle():
    def __init__(self, map, size: int):
        self.map = map
        self.size = size
        self.index = self.getIndex()

    def __str__(self):
        result = ""
        for index, value in enumerate(self.map):
            result += str(value) + " | "
            if (index + 1) % self.size == 0:
                result += "\n"

        return result

    def __eq__(self, value):
        return self.map == value.map

    def getIndex(self):
        for index, value in enumerate(self.map):
            if (value == 0):
                return index

        return None

    def getIndexCoords(self, index):
        row = int(index / self.size)

        column = index % self.size

        return column, row