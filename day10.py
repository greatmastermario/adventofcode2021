import adventutils
import statistics


def part1(file):
    print("Part 1")
    lines = adventutils.file_contents(file)
    score = 0
    for line in lines:
        score += iscorrupted(line)
    print(score)


def part2(file):
    print("Part 2")
    lines = adventutils.file_contents(file)
    scores = list()
    for line in lines:
        if iscorrupted(line) == 0:
            scores.append(autocomplete(line))
    print(statistics.median(scores))


def iscorrupted(line):
    parser = list()
    for char in line:
        if char in ["{", "[", "(", "<"]:
            parser.append(char)
        else:
            previouschar = parser.pop()
            if previouschar == "(" and char != ")":
                return corruptscore(char)
            elif previouschar == "[" and char != "]":
                return corruptscore(char)
            elif previouschar == "{" and char != "}":
                return corruptscore(char)
            elif previouschar == "<" and char != ">":
                return corruptscore(char)
    return 0


def autocomplete(line):
    parser = list()
    for char in line:
        if char in ["{", "[", "(", "<"]:
            parser.append(char)
        else:
            parser.pop()
    return autocompletescore(parser)


def corruptscore(char):
    if char == ")":
        return 3
    elif char == "]":
        return 57
    elif char == "}":
        return 1197
    elif char == ">":
        return 25137


def autocompletescore(parser):
    score = 0
    parser.reverse()
    for char in parser:
        score *= 5
        if char == "(":
            score += 1
        elif char == "[":
            score += 2
        elif char == "{":
            score += 3
        elif char == "<":
            score += 4
    return score


if __name__ == "__main__":
    part1("./data/day10part1.txt")
    part2("./data/day10part1.txt")
