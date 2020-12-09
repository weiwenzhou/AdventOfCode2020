array = [int(x) for x in open("input.txt").read().splitlines()]


def sum1(start, end):
    sums = set()
    for x in range(start, end):
        for y in range(start,end):
            if x != y:
                sums.add(array[x]+array[y])
    return sums

def part1():
    for i, x in enumerate(array[25:]):
        if x not in sum1(i, i+25):
            return x



def part2(weak):
    for i in range(len(array)):
        for j in range(len(array)):
            temp = array[i:j]
            if sum(temp) == weak:
                return min(temp) + max(temp)
print(part1())
print(part2(part1()))