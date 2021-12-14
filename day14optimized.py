import adventutils


def part1(file):
    print("Part 1")
    runpolymer(10, file)


def part2(file):
    print("Part 2")
    runpolymer(40, file)


def templateandpairs(contents):
    template = contents[0]
    pairs = dict()
    for index in range(2, len(contents)):
        pair, result = contents[index].split(" -> ")
        pairs[pair] = result
    return template, pairs


def recursivepolymer(template, pairs, depth, counts):
    if depth == 0:
        for char in range(0, 2):
            if template[char] in counts.keys():
                counts[template[char]] += 1
            else:
                counts[template[char]] = 1
        return
    # lastchar = template[-1]
    for index in range(0, len(template) - 1):
        pair = template[index:index + 2]
        recursivepolymer(pair[0] + pairs[pair] + pair[1], pairs, depth - 1, counts)
    # if lastchar in counts.keys():
    #     counts[lastchar] += 1
    # else:
    #     counts[lastchar] = 1


def minmax(charcounts):
    min = 1000000000000000
    max = -1
    for count in charcounts.values():
        if count < min:
            min = count
        if count > max:
            max = count
    return min, max


def runpolymer(iterations, file):
    contents = adventutils.file_contents(file)
    template, pairs = templateandpairs(contents)
    counts = dict()
    recursivepolymer(template, pairs, iterations, counts)
    lastchar = template[-1]
    if lastchar in counts.keys():
        counts[lastchar] += 1
    else:
        counts[lastchar] = 1
    minimum, maximum = minmax(counts)
    print(maximum - minimum)


if __name__ == "__main__":
    part1("./data/day14part1.txt")
    part2("./data/day14part1.txt")
