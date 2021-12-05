import adventutils


def part1(file):
    print("Part 1")
    lines = adventutils.file_contents(file)
    coords = split_coords(lines)
    coord_count = {}
    for coord in coords:
        if horizontal(coord[0], coord[1]):
            add_horizontal(coord_count, coord[0][0], coord[1][0], coord[0][1])
        elif vertical(coord[0], coord[1]):
            add_vertical(coord_count, coord[0][0], coord[0][1], coord[1][1])
    print_danger(coord_count)


def part2(file):
    print("Part 2")
    lines = adventutils.file_contents(file)
    coords = split_coords(lines)
    coord_count = {}
    for coord in coords:
        if horizontal(coord[0], coord[1]):
            add_horizontal(coord_count, coord[0][0], coord[1][0], coord[0][1])
        elif vertical(coord[0], coord[1]):
            add_vertical(coord_count, coord[0][0], coord[0][1], coord[1][1])
        else:
            add_diagonal(coord_count, coord[0][0], coord[1][0], coord[0][1], coord[1][1])
    print_danger(coord_count)


def horizontal(a, b):
    return a[1] == b[1]


def vertical(a, b):
    return a[0] == b[0]


def split_coords(lines):
    coords = list()
    for line in lines:
        split_line = line.split(" -> ")
        a = split_line[0].split(",")
        b = split_line[1].split(",")
        coords.append([(a[0], a[1]), (b[0], b[1])])
    return coords


def add_horizontal(coord_counts, x1, x2, y):
    x1int = int(x1)
    x2int = int(x2)
    for x in range(min(x1int, x2int), max(x1int, x2int) + 1):
        coord = (x, int(y))
        if coord not in coord_counts.keys():
            coord_counts[coord] = 1
        else:
            coord_counts[coord] = coord_counts[coord] + 1


def add_vertical(coord_counts, x, y1, y2):
    y1int = int(y1)
    y2int = int(y2)
    for y in range(min(y1int, y2int), max(y1int, y2int) + 1):
        coord = (int(x), y)
        if coord not in coord_counts.keys():
            coord_counts[coord] = 1
        else:
            coord_counts[coord] = coord_counts[coord] + 1


def add_diagonal(coord_counts, x1, x2, y1, y2):
    x1int = int(x1)
    x2int = int(x2)
    y1int = int(y1)
    y2int = int(y2)
    startx = min(x1int, x2int)
    currenty = y1int
    if startx == x2int:
        currenty = y2int
    dy = -1
    if (x1int > x2int and y1int > y2int) or (x2int > x1int and y2int > y1int):
        dy = 1
    for x in range(min(x1int, x2int), max(x1int, x2int) + 1):
        coord = (x, currenty)
        if coord not in coord_counts.keys():
            coord_counts[coord] = 1
        else:
            coord_counts[coord] = coord_counts[coord] + 1
        currenty += dy


def print_danger(coord_count):
    danger = 0
    for count in coord_count.values():
        if count >= 2:
            danger += 1
    print(danger)


if __name__ == "__main__":
    part1("./data/day5part1.txt")
    part2("./data/day5part1.txt")
