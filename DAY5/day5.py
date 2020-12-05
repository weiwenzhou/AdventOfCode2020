array = [x for x in open("input.txt").read().splitlines()]

def part1():
    answer = 0
    for x in array:
        xVal = 0
        yVal = 0
        row = x[:-3]
        col = x[-3:]
        for ri, r in enumerate(row):
            xVal += 2 ** ri if r == "B" else 0
        for ci, c in enumerate(col):
            yVal += 2 ** ci if c == "R" else 0
        temp = xVal * 8 + yVal
        if temp > answer:
            answer = temp

    return answer


def part2():
    stuff = set()
    answer = 0
    for x in array:
        xVal = 0
        yVal = 0
        row = x[:-3]
        col = x[-3:]
        for ri, r in enumerate(row):
            xVal += 2 ** ri if r == "B" else 0
        for ci, c in enumerate(col):
            yVal += 2 ** ci if c == "R" else 0
        temp = xVal * 8 + yVal
        stuff.add(temp)

    # last = set(range(896)) - stuff
    stuff = list(stuff)
    stuff.sort()
    for x in range(stuff[0], stuff[-1]):
        if x not in stuff and x-1 in stuff and x+1 in stuff:
            print(x,"Ssds")

    return len(stuff)


seats = set()
for line in [x.strip() for x in open("input.txt", "r").readlines()]:
    row = sum([2**i for i, x in enumerate(line[0:7][::-1]) if x == "B"])
    seat = sum([2**i for i, x in enumerate(line[7:10][::-1]) if x == "R"])
    seatid = row * 8 + seat
    seats.add(seatid)

for i in range(max(seats)):
    if i not in seats and i + 1 in seats and i - 2 in seats:
        print(i)

print(part1())

print("SPSKSF")
print(part2())

print(len(seats))