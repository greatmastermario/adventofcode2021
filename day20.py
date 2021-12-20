import adventutils


def part1(file):
    print("Part 1")
    algo, inputimage = getalgoandinput(adventutils.file_contents(file))
    infinitepixel = "."
    for _ in range(2):
        inputimage, infinitepixel = enhance(algo, inputimage, infinitepixel)
    print(countpixels(inputimage, "#"))
    print("Part 2")
    for _ in range(2, 50):
        inputimage, infinitepixel = enhance(algo, inputimage, infinitepixel)
    print(countpixels(inputimage, "#"))


def getalgoandinput(contents):
    algo = [char for char in contents[0]]
    inputimage = list()
    for line in contents[2:]:
        inputimage.append([char for char in line])
    return algo, inputimage


def enhance(algo, inputimage, infinitepixel):
    outputimage = [[getpixel(algo, inputimage, x, y, infinitepixel) for y in range(0, len(inputimage[0]) + 2)]
                   for x in range(0, len(inputimage) + 2)]
    infinitepixel = algo[0] if infinitepixel == "." else algo[511]
    return outputimage, infinitepixel


def getpixel(algo, inputimage, xindex, yindex, infinitepixel):
    algoindex = ""
    for x in range(xindex - 2, xindex + 1):
        for y in range(yindex - 2, yindex + 1):
            if x not in range(0, len(inputimage)) or y not in range(0, len(inputimage[x])):
                algoindex += "0" if infinitepixel == "." else "1"
            else:
                algoindex += "0" if inputimage[x][y] == "." else "1"
    return algo[int(algoindex, 2)]


def countpixels(inputimage, pixeltofind):
    count = 0
    for line in inputimage:
        for pixel in line:
            if pixel == pixeltofind:
                count += 1
    return count


if __name__ == "__main__":
    part1("./data/day20part1.txt")
