array = [[c for c in x] for x in open("input.txt").read().splitlines()]

def part1():
    answer = 0
    # 3 1
    x = 0
    y = 0
    lenX = len(array[0])
    lenY = len(array)
    while x < lenX and y < lenY:
        if array[y][x] == '#':
            answer += 1
        y += 1
        x = (x+3) % lenX

    return answer


def part2(xc, yc):
    answer = 0
    x = 0
    y = 0
    lenX = len(array[0])
    lenY = len(array)
    while x < lenX and y < lenY:
        if array[y][x] == '#':
            answer += 1
        y += yc
        x = (x+xc) % lenX

    return answer



print(part1())
# print(part2())
print(part2(1,1) * part2(3,1) * part2(5,1) * part2(7,1) * part2(1,2))
print(part2(1,1),part2(3,1),part2(5,1),part2(7,1),part2(1,2))
