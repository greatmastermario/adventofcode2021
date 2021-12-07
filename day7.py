import math
import statistics

import adventutils

fuelcache = dict()


def part1(file):
    print("Part 1")
    crabposlist = adventutils.file_contents(file)
    crabs = [int(crab) for crab in crabposlist[0].split(",")]
    crabs.sort()
    median = int(statistics.median(crabs))
    fueltotal = 0
    for crab in crabs:
        fueltotal += abs(crab - median)
    print(fueltotal)


def part2(file):
    print("Part 2")
    crabposlist = adventutils.file_contents(file)
    crabs = [int(crab) for crab in crabposlist[0].split(",")]
    average = statistics.mean(crabs)
    fueltotal = 0
    fueltotalfloor = 0
    for crab in crabs:
        fueltotal += crabfuel(abs(crab - math.ceil(average)))
        fueltotalfloor += crabfuel(abs(crab - math.floor(average)))
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
