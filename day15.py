import sys

import adventutils


def part1(file):
    print("Part 1")
    riskvals = risks(adventutils.file_contents(file))
    totalrisk = djikstra(riskvals)
    print(totalrisk[-1][-1])


def part2(file):
    print("Part 2")
    riskvals = bigrisks(adventutils.file_contents(file))
    totalrisk = djikstra(riskvals)
    print(totalrisk[-1][-1])


def risks(contents):
    return [[int(y) for y in x] for x in contents]


def bigrisks(contents):
    baserisks = risks(contents)
    allrisks = list()
    for x in range(len(baserisks) * 5):
        row = list()
        for y in range(len(baserisks) * 5):
            val = baserisks[x % len(baserisks)][y % len(baserisks)] + x // len(baserisks) + y // len(baserisks)
            if val > 9:
                val -= 9
            row.append(val)
        allrisks.append(row)
    return allrisks


def djikstra(riskvals):
    totalrisk = [[None for _ in range(len(x))] for x in riskvals]
    seen = set()
    pending = set()
    pending.add((0, 0))
    totalrisk[0][0] = 0
    while (len(riskvals) - 1, len(riskvals[-1]) - 1) not in seen:
        x, y = minnotseen(totalrisk, pending)
        seen.add((x, y))
        pending.remove((x, y))
        if x > 0:
            setrisk(totalrisk, riskvals, x - 1, y, totalrisk[x][y], seen, pending)
        if x < len(totalrisk) - 1:
            setrisk(totalrisk, riskvals, x + 1, y, totalrisk[x][y], seen, pending)
        if y > 0:
            setrisk(totalrisk, riskvals, x, y - 1, totalrisk[x][y], seen, pending)
        if y < len(totalrisk[x]) - 1:
            setrisk(totalrisk, riskvals, x, y + 1, totalrisk[x][y], seen, pending)
    return totalrisk


def minnotseen(totalrisk, pending):
    minx = None
    miny = None
    minrisk = sys.maxsize
    for x, y in pending:
        if totalrisk[x][y] < minrisk:
            minx = x
            miny = y
            minrisk = totalrisk[x][y]
    return minx, miny


def setrisk(totalrisk, riskvals, x, y, previousrisk, seen, pending):
    if (x, y) not in seen and (totalrisk[x][y] is None or totalrisk[x][y] > previousrisk + riskvals[x][y]):
        totalrisk[x][y] = previousrisk + riskvals[x][y]
        pending.add((x, y))


if __name__ == "__main__":
    part1("./data/day15part1.txt")
    part2("./data/day15part1.txt")
