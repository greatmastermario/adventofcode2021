import adventutils


def part1(file):
    print("Part 1")
    lines = adventutils.file_contents(file)
    heightmap = list()
    for line in lines:
        heightmap.append([int(height) for height in line])
    risktotal = 0
    for x in range(0, len(heightmap)):
        for y in range(0, len(heightmap[x])):
            if islowpoint(heightmap, x, y):
                risktotal += heightmap[x][y] + 1
    print(risktotal)


def part2(file):
    print("Part 2")
    lines = adventutils.file_contents(file)
    heightmap = list()
    for line in lines:
        heightmap.append([int(height) for height in line])
    basinsizes = list()
    for x in range(0, len(heightmap)):
        for y in range(0, len(heightmap[x])):
            if islowpoint(heightmap, x, y):
                basinsizes.append(getbasinsize(heightmap, x, y))
    basinsizes.sort(reverse=True)
    print(basinsizes[0] * basinsizes[1] * basinsizes[2])


def islowpoint(heightmap, x, y):
    height = heightmap[x][y]
    if x > 0 and heightmap[x - 1][y] <= height:
        return False
    elif x < len(heightmap) - 1 and heightmap[x + 1][y] <= height:
        return False
    elif y > 0 and heightmap[x][y - 1] <= height:
        return False
    elif y < len(heightmap[x]) - 1 and heightmap[x][y + 1] <= height:
        return False
    return True


def getbasinsize(heightmap, x, y):
    return len(getpoints(heightmap, x, y, set()))


def getpoints(heightmap, x, y, foundpoints):
    if (x, y) in foundpoints or x < 0 or y < 0 or x >= len(heightmap) or y >= len(heightmap[x]) or heightmap[x][y] == 9:
        return foundpoints
    foundpoints.add((x, y))
    getpoints(heightmap, x + 1, y, foundpoints)
    getpoints(heightmap, x - 1, y, foundpoints)
    getpoints(heightmap, x, y + 1, foundpoints)
    getpoints(heightmap, x, y - 1, foundpoints)
    return foundpoints


if __name__ == "__main__":
    # part1("./data/part9test.txt")
    part1("./data/day9part1.txt")
    part2("./data/day9part1.txt")
