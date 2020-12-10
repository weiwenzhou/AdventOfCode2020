array = [int(x) for x in open("input.txt").read().splitlines()]

array.append(max(array)+3)
array = sorted(array)

def part1():
    one = 1
    three = 0
    cur = array[0]
    for x in array:
        if x - cur == 1:
            one += 1
        elif x - cur == 3:
            three += 1
        cur = x
    print(one, three)
    return one * three

def addToRange(arr, start, end):
    for x in range(end-start):
        arr[x+start] += 1

def part2(data):
    # holder = [0]*len(array)
    # one = 0
    # three = 1
    # m = max(array) + 3
    # cur = 0
    # for i, x in enumerate(array):
    #     if x+3 in array:
    #         t = array.index(x+3)
    #         addToRange(holder, i, t-1)


    # return eval("*".join([str(x) for x in holder if x != 0]))


    from bisect import bisect_left
    n=len(data)
    dp=[0]*n
    for i in range(n):
        if data[i]<=3:
            dp[i]=2**i
            continue
        ind=bisect_left(data,data[i]-3)
        dp[i]=sum(dp[ind:i])

    return (dp[-1])

print(part1())
print(part2(array))

