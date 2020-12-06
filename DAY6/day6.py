
array = [x for x in open("input.txt").read().split("\n\n")]

def part1():
    answer = 0
    for x in array:
        answer += len(set(c for c in x if 'a' <= c <= 'z'))


    return answer


def part2():
    answer = 0
    for x in array:
        splitTemp = x.split("\n")
        temp = set([a for a in "qwertyuiopasdfghjklzxcvbnm"])
        for person in splitTemp:
            temp &= set(c for c in person if 'a' <= c <= 'z')
        answer += len(temp)
    return answer


print(part1())
print(part2())