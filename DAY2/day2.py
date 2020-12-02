array = [x for x in open("input.txt").read().splitlines()]


def part1():
    answer = 0
    for x in array:
        
        x = x.split(":")
        string = x[1]
        y = x[0].split(" ")
        z = y[0].split("-")
        count = string.count(y[1].strip())
        if count < int(z[0]) or count >int(z[1]):
            answer += 1
    return len(array) - answer


def part2():
    answer = 0


    for x in array:
        
        x = x.split(":")
        string = x[1]
        y = x[0].split(" ")
        z = y[0].split("-")
        count = string.count(y[1].strip())
        if (string[int(z[0])] == y[1].strip() and string[int(z[1])] == y[1].strip()) or (string[int(z[0])] != y[1].strip() and string[int(z[1])] != y[1].strip()):
            answer += 1

    return len(array) - answer


print(part1())
print(part2())