import re
array = [x for x in open("input.txt").read().splitlines()]

def part1():
    answer = 0
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    for x in array:
        if x == "":
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                answer += 1
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
        else:
            if "byr:" in x:
                byr = True
            if "iyr:" in x:
                iyr = True
            if "eyr:" in x:
                eyr = True
            if "hgt:" in x:
                hgt = True
            if "hcl:" in x:
                hcl = True
            if "ecl:" in x:
                ecl = True
            if "pid:" in x:
                pid = True

    return answer


def part2():
    answer = 0
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    for y in array:
        if y == "":
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                answer += 1
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
        else:
            y = y.split(" ")
            for x in y: 
                if "byr:" in x:
                    val = int(x.split(":")[1])
                    if val >= 1920 and val <= 2002:
                        byr = True
                if "iyr:" in x:
                    val = int(x.split(":")[1])
                    if val >= 2010 and val <= 2020:
                        iyr = True
                if "eyr:" in x:
                    val = int(x.split(":")[1])
                    if val >= 2020 and val <= 2030:
                        eyr = True
                if "hgt:" in x:
                    val = x.split(":")[1]
                    ext = val[-2:]
                    if ext == "cm":
                        val = int(val[:-2])
                        if val >= 150 and val <= 193:
                            hgt = True
                    if ext == "in":
                        val = int(val[:-2])
                        if val >= 59 and val <= 76:
                            hgt = True
                if "hcl:" in x:
                    val = x.split(":")[1]
                    if len(val) == 7 and val[0] == "#" and bool(re.match(r"[0-9a-f]", val[1:])):
                        hcl = True
                if "ecl:" in x:
                    val = x.split(":")[1]
                    ecolor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if val in ecolor:
                        ecl = True
                if "pid:" in x:
                    val = x.split(":")[1]
                    if len(val) == 9 and bool(re.match(r"[0-9]", val)):
                        pid = True
    return answer


print(part1())
print(part2())
