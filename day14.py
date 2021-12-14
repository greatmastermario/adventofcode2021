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


def recursivepolymer(template, pairs, depth):
    counts = dict()
    for index in range(len(template) - 1):
        key = template[index] + template[index + 1]
        if key in counts.keys():
            counts[key] += 1
        else:
            counts[key] = 1
    for _ in range(depth):
        itercounts = dict()
        for pair, count in counts.items():
            firstkey = pair[0] + pairs[pair]
            secondkey = pairs[pair] + pair[1]
            if firstkey in itercounts.keys():
                itercounts[firstkey] += count
            else:
                itercounts[firstkey] = count
            if secondkey in itercounts.keys():
                itercounts[secondkey] += count
            else:
                itercounts[secondkey] = count
        counts = itercounts
    finalcounts = dict()
    for pair, count in counts.items():
        if pair[0] in finalcounts:
            finalcounts[pair[0]] += count
        else:
            finalcounts[pair[0]] = count
    finalcounts[template[-1]] += 1
    return finalcounts


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
    counts = recursivepolymer(template, pairs, iterations)
    minimum, maximum = minmax(counts)
    print(maximum - minimum)


if __name__ == "__main__":
    part1("./data/day14part1.txt")
    part2("./data/day14part1.txt")
