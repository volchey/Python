#/usr/bin/python

def countHeuristicWeight(puzzle):
    result = 0
    for index, value in enumerate(puzzle):
        if index + 1 != value:
            result += 1
    return result

# def moveCurrentPosition
     