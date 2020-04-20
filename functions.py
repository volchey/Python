#/usr/bin/python

def getIndexCoords(index: int, size: int):
    if (size == 0):
        return
    row = int(index / size)

    column = index % size

    return column, row

def countHeuristicWeight(puzzle):
    result = 0
    for index, value in enumerate(puzzle):
        if index + 1 != value:
            result += 1
    return result

# def moveCurrentPosition
     