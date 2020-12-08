array = [x for x in open("input.txt").read().splitlines()]

accumulator = 0

def part1(num, value, done):
    if num in done:
        return value
    done.add(num)
    x = array[num]
    if "acc" in x:
        value += int(x.split(" ")[1])
        return part1(num+1, value, done)
    elif "jmp" in x:
        return part1(num+int(x.split(" ")[1]), value, done)
    else:
        return part1(num+1, value, done)

def part2(num, value, done):
    if num > len(array):
        return False
    if num in done:
        return False
    if num == len(array):
        return value
    done.add(num)
    x = array[num]
    if "acc" in x:
        value += int(x.split(" ")[1])
        return part2(num+1, value, done)
    elif "jmp" in x:
        return part2(num+int(x.split(" ")[1]), value, done)
    else:
        return part2(num+1, value, done)



print(part1(0, 0, set()))
# print(part2(0, 0, set()))

for i in range(len(array)):
    if "jmp" in array[i]:
        array[i] = array[i].replace("jmp", "nop")
        value = part2(0, 0, set())
        if value is not False:
            print(value)
            break 
        array[i] = array[i].replace("nop", "jmp")
    elif "nop" in array[i]:
        array[i] = array[i].replace("nop", "jmp")
        value = part2(0, 0, set())
        if value is not False:
            print(value)
            break 
        array[i] = array[i].replace("jmp", "nop")