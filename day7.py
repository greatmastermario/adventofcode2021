import math

import adventutils

fuelcache = dict()


def part1(file):
    print("Part 1")
    crabposlist = adventutils.file_contents(file)
    crabs = [int(crab) for crab in crabposlist[0].split(",")]
    total = 0
    for crab in crabs:
        total += crab
    crabs.sort()
    median = 0
    if len(crabs) % 2 == 1:
        median = crabs[math.floor(len(crabs)/2)]
    else:
        median = (crabs[int(len(crabs) / 2)] + crabs[int(len(crabs) / 2 - 1)]) / 2
    fueltotal = 0
    for crab in crabs:
        fueltotal += abs(crab - median)
    print(fueltotal)


def part2(file):
    print("Part 2")
    crabposlist = adventutils.file_contents(file)
    crabs = [int(crab) for crab in crabposlist[0].split(",")]
    total = 0
    for crab in crabs:
        total += crab
    average = math.ceil(total / len(crabs))
    averagefloor = math.floor(total / len(crabs))
    fueltotal = 0
    fueltotalfloor = 0
    for crab in crabs:
        fueltotal += crabfuel(abs(crab - average))
        fueltotalfloor += crabfuel(abs(crab - averagefloor))
    print(min(fueltotal, fueltotalfloor))


def crabfuel(num):
    total = 0
    if num in fuelcache.keys():
        return fuelcache[num]
    elif num == 0:
        return 0
    for step in range(1, num + 1):
        total += step
    fuelcache[num] = total
    return total


if __name__ == "__main__":
    part1("./data/day7part1.txt")
    part2("./data/day7part1.txt")
