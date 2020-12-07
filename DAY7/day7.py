from collections import Counter

array = [x for x in open("input.txt").read().splitlines()]

bags = set()

def part1(word):
    global bags
    for x in array:
        y = x.split(" contain ")
        for t in y[1].split(","):
            if word in t:
                part1(y[0][:-5])
                bags.add(y[0])


def part2(word):
    answer = 0
    for x in array:
        y = x.split(" contain ")
        if word in y[0]:
            if "no other bags" not in y[1]:
                for t in y[1][:-1].split(","):
                    temp = t.strip().split(" ")
                    count = temp[0]
                    name = temp[1:]
                    answer += int(count)*part2(" ".join(name))
    return answer+1


part1("shiny gold")
print("part1", len(bags))
print(part2("shiny gold")-1)