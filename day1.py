import adventutils


def part1(file):
    print("Part 1")
    # print(adventutils.file_contents(file))
    depths = adventutils.file_contents(file)
    increasecount = 0
    previousdepth = None
    for currentdepth in depths:
        currentdepth = int(currentdepth)
        if previousdepth is not None and currentdepth > previousdepth:
            increasecount += 1
        previousdepth = currentdepth
    print(increasecount)


def part2(file):
    print("Part 2")
    # print(adventutils.file_contents(file))
    depths = adventutils.file_contents(file)
    increasecount = 0
    previousdepth = None
    for index in range(2, len(depths)):
        currentdepth = int(depths[index]) + int(depths[index - 1]) + int(depths[index - 2])
        if previousdepth is not None and currentdepth > previousdepth:
            increasecount += 1
        previousdepth = currentdepth
    print(increasecount)


if __name__ == "__main__":
    part1("./data/day1part1.txt")
    part2("./data/day1part1.txt")
