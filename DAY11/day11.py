from copy import deepcopy
from pprint import pprint

array = [[c for c in x] for x in open("input.txt").read().splitlines()]

def check(r, c):
    if r >= 0 and r < len(array) and c >= 0 and c < len(array[0]):
        if array[r][c] == "#":
            return 1
    return 0

def checkAdjacent(r, c):
    # part 1
    # total = check(r-1, c-1) + check(r-1, c) + check(r-1, c+1) + check(r+1, c-1) + check(r+1, c) + check(r+1, c+1) + check(r, c-1) + check(r, c+1)
    total = 0 
    directions = [(-1,-1), (-1, 0), (-1, 1), (1,-1), (1,0), (1,1), (0, -1), (0, 1)]
    for d in directions:
        x = r
        y = c
        notFound = True
        while x >= 0 and x < len(array) and y >= 0 and y < len(array[0]) and notFound:
            x += d[0]
            y += d[1]
            if x >= 0 and x < len(array) and y >= 0 and y < len(array[0]):
                total += check(x,y)
                if array[x][y] == "#" or array[x][y] == "L":
                    notFound = False


    return total

while True:
    temp = deepcopy(array)
    # pprint(array)
    # print()
    for r, row in enumerate(array):
        for c, col in enumerate(row):
            if col == "L":
                if checkAdjacent(r,c) == 0:
                    temp[r][c] = "#"
            elif col == "#":
                if checkAdjacent(r,c) >= 5:
                    temp[r][c] = "L"
    if array == temp:
        array = temp
        break
    array = temp

total = "".join(["".join(row) for row in array])
total = total.replace("L","")
total = total.replace(".","")
print("ANSWER", total.count("#"))