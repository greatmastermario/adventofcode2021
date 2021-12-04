import adventutils


def part1(file):
    print("Part 1")
    readings = adventutils.file_contents(file)
    counts = list()
    for index in range(0, len(readings[0])):
        counts.append(0)
    for reading in readings:
        for index in range(0, len(reading)):
            counts[index] += int(reading[index])
    gamma = ""
    epsilon = ""
    for count in counts:
        if count > len(readings) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon)


def part2(file):
    print("Part 2")
    readings = adventutils.file_contents(file)
    # oxygen
    oxygenreadings = readings
    for pos in range(0, len(readings)):
        bit = most_common_bit(oxygenreadings, pos)
        oxygenreadings = filter_bit(oxygenreadings, pos, bit)
        if len(oxygenreadings) == 1:
            break
    co2readings = readings
    for pos in range(0, len(readings)):
        bit = least_common_bit(co2readings, pos)
        co2readings = filter_bit(co2readings, pos, bit)
        if len(co2readings) == 1:
            break
    print(int(oxygenreadings[0], 2) * int(co2readings[0], 2))


def most_common_bit(readings, pos):
    count = 0
    for reading in readings:
        count += int(reading[pos])
    if count >= len(readings) / 2:
        return "1"
    return "0"


def least_common_bit(readings, pos):
    count = 0
    for reading in readings:
        count += int(reading[pos])
    if count < len(readings) / 2:
        return "1"
    return "0"


def filter_bit(readings, pos, bit):
    filtered = list()
    for reading in readings:
        if reading[pos] == bit:
            filtered.append(reading)
    return filtered


if __name__ == "__main__":
    part1("./data/day3part1.txt")
    part2("./data/day3part1.txt")
