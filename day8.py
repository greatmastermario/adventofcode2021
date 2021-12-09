import adventutils


def part1(file):
    print("Part 1")
    filecontents = adventutils.file_contents(file)
    displays = getdisplays(filecontents)
    outputs = [display[1] for display in displays]
    print(scanoutput(outputs))


def part2(file):
    print("Part 2")
    filecontents = adventutils.file_contents(file)
    displays = getdisplays(filecontents)
    total = 0
    for display in displays:
        mapping = getmapping(display[0])
        total += int(displayvalue(mapping, display[1]))
    print(total)


def scanoutput(output):
    count = 0
    for line in output:
        for num in line:
            if isunique(num):
                count += 1
    return count


def isunique(num):
    return len(num) in [2, 3, 4, 7]


def getdisplays(filecontents):
    displays = list()
    for line in filecontents:
        splitline = line.split(" | ")
        displays.append((splitline[0].split(" "), splitline[1].split(" ")))
    return displays


def getmapping(inputs):
    mapping = dict()
    mapping[1] = get1(inputs)
    mapping[4] = get4(inputs)
    mapping[7] = get7(inputs)
    mapping[8] = get8(inputs)
    mapping["a"] = geta(mapping[7], mapping[1])
    mapping[9] = get9(mapping[4], mapping["a"], inputs)
    mapping[3] = get3(mapping[9], mapping[1], inputs)
    mapping[5] = get5(mapping[9], mapping[3], inputs)
    mapping[2] = get2(mapping[5], mapping[3], inputs)
    mapping["c"] = getc(mapping[9], mapping[5])
    mapping[6] = get6(mapping["c"], inputs)
    mapping[0] = get0(mapping[6], mapping[9], inputs)
    return mapping
    
    
def get1(inputs):
    for num in inputs:
        if len(num) == 2:
            return sort(num)


def get4(inputs):
    for num in inputs:
        if len(num) == 4:
            return sort(num)


def get7(inputs):
    for num in inputs:
        if len(num) == 3:
            return sort(num)


def get8(inputs):
    for num in inputs:
        if len(num) == 7:
            return sort(num)


def geta(map7, map1):
    for char in map7:
        if char not in map1:
            return [char]


def get9(map4, mapa, inputs):
    include = map4 + mapa
    for num in inputs:
        if len(num) == 6 and valid9(include, num):
            return sort(num)


def valid9(include, num):
    matches = 0
    for char in num:
        if char in include:
            matches += 1
    return matches == len(include)


def get5(map9, map3, inputs):
    for num in inputs:
        if len(num) == 5 and valid5(map9, map3, num):
            return sort(num)


def valid5(map9, map3, num):
    for char in num:
        if char not in map9:
            return False
    return sort(num) != map3


def get3(map9, map1, inputs):
    for num in inputs:
        if len(num) == 5 and valid3(map9, map1, num):
            return sort(num)


def valid3(map9, map1, num):
    for char in num:
        if char not in map9:
            return False
    for char in map1:
        if char not in num:
            return False
    return True


def getc(map9, map5):
    for char in map9:
        if char not in map5:
            return [char]


def get2(map5, map3, inputs):
    for num in inputs:
        if len(num) == 5 and sort(num) not in [map5, map3]:
            return sort(num)


def get6(mapc, inputs):
    for num in inputs:
        if len(num) == 6 and mapc[0] not in sort(num):
            return sort(num)


def get0(map6, map9, inputs):
    for num in inputs:
        if len(num) == 6 and sort(num) not in [map6, map9]:
            return sort(num)


def displayvalue(mapping, output):
    value = ""
    for num in output:
        for key in mapping.keys():
            if sort(num) == mapping[key]:
                value += str(key)
                break
    return value


def sort(numstr):
    sorted = [char for char in numstr]
    sorted.sort()
    return sorted


if __name__ == "__main__":
    part1("./data/day8part1.txt")
    part2("./data/day8part1.txt")
