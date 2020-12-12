array = [x for x in open("input.txt").read().splitlines()]

directions = {  'N': (0, 1), 
                'S': (0, -1),
                'E': (1, 0),
                'W': (-1, 0)}
collection = {}
def part1():
    x = 0
    y = 0
    direction = 'E'
    dx, dy = 1, 0
    for line in array:
        for d, val in directions.items():
            if d in line:
                tdx, tdy = val
                x += tdx * int(line[1:])
                y += tdy * int(line[1:])
        if 'F' in line:
            x += dx * int(line[1:])
            y += dy * int(line[1:])
        if 'L' in line:
            order = ['N', 'W', 'S', 'E']
            deg = int(line[1:])/90 
            direction = order[int((order.index(direction)+deg)%4)]
            dx, dy = directions[direction]
        if 'R' in line:
            order = ['N', 'E', 'S', 'W']
            deg = int(line[1:])/90 
            direction = order[int((order.index(direction)+deg)%4)]
            dx, dy = directions[direction]

    return abs(x)+abs(y)


def part2():
    x = 0
    y = 0
    direction = {'N': 1, 'E':10, 'S':0, 'W':0}
    for num, line in enumerate(array):
        for d, val in directions.items():
            if d in line:
                direction[d] += int(line[1:]) 
        if 'F' in line:
            for d, val in directions.items():
                tdx, tdy = val
                x += tdx * int(line[1:]) * direction[d]
                y += tdy * int(line[1:]) * direction[d]
        if 'L' in line:
            deg = int(line[1:])
            order = ['N', 'W', 'S', 'E']
            order_new = ['W', 'S', 'E', 'N'] if deg == 90 else ['S', 'E', 'N', 'W'] if deg == 180 else ['E', 'N', 'W', 'S'] if deg == 270 else ['N', 'W', 'S', 'E']
            temp = {}
            for old, new in zip(order, order_new):
                temp[new] = direction[old]
            direction = temp
        if 'R' in line:
            deg = int(line[1:])
            order = ['N', 'E', 'S', 'W']
            order_new = ['E', 'S', 'W', 'N'] if deg == 90 else ['S', 'W', 'N', 'E',] if deg == 180 else ['W', 'N', 'E', 'S'] if deg == 270 else ['N', 'E', 'S', 'W']
            temp = {}
            for old, new in zip(order, order_new):
                temp[new] = direction[old]
            direction = temp
        collection[num] = x,y
    return abs(x)+abs(y)


print(part1())
print(part2())
