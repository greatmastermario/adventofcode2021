import adventutils


def part1(file):
    print("Part 1")
    grid = [[int(char) for char in line] for line in adventutils.file_contents(file)]
    flashcount = 0
    for _ in range(100):
        flashcount += step(grid)
    print(flashcount)


def part2(file):
    print("Part 2")
    grid = [[int(char) for char in line] for line in adventutils.file_contents(file)]
    steps = 0
    while not issynced(grid):
        steps += 1
        step(grid)
    print(steps)


def step(grid):
    flashcount = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] += 1
            if grid[x][y] == 10:
                flashcount += flash(grid, x, y)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] >= 10:
                grid[x][y] = 0
    return flashcount


def flash(grid, x, y):
    flashcount = 1
    for flashx in range(x - 1, x + 2):
        for flashy in range(y - 1, y + 2):
            if flashx < 0 or flashx >= len(grid) or flashy < 0 or flashy >= len(grid[x]):
                continue
            grid[flashx][flashy] += 1
            if grid[flashx][flashy] == 10:
                flashcount += flash(grid, flashx, flashy)
    return flashcount


def issynced(grid):
    for row in grid:
        for column in row:
            if column != 0:
                return False
    return True


if __name__ == "__main__":
    part1("./data/day11part1.txt")
    part2("./data/day11part1.txt")
