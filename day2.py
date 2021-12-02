import adventutils


def part1(file):
    print("Part 1")
    directions = adventutils.file_contents(file)
    horizontal = 0
    depth = 0
    for direction in directions:
        split = direction.split(" ")
        way = split[0]
        distance = int(split[1])
        if way == "forward":
            horizontal += distance
        elif way == "up":
            depth -= distance
        elif way == "down":
            depth += distance
    print(horizontal * depth)


def part2(file):
    print("Part 2")
    directions = adventutils.file_contents(file)
    horizontal = 0
    depth = 0
    aim = 0
    for direction in directions:
        split = direction.split(" ")
        way = split[0]
        distance = int(split[1])
        if way == "forward":
            horizontal += distance
            depth += aim * distance
        elif way == "up":
            aim -= distance
        elif way == "down":
            aim += distance
    print(horizontal * depth)


if __name__ == "__main__":
    part1("./data/day2part1.txt")
    part2("./data/day2part1.txt")
