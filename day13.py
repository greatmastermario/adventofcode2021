import adventutils
import pprint


def part1(file):
    print("Part 1")
    contents = adventutils.file_contents(file)
    coords, folds = coordsandfolds(contents)
    coords = fold(coords, folds[0])
    print(len(coords))


def part2(file):
    print("Part 2")
    contents = adventutils.file_contents(file)
    coords, folds = coordsandfolds(contents)
    for instr in folds:
        coords = fold(coords, instr)
    print(len(coords))
    for coord in coords:
        print(coord)
    # TODO How to do this without manually using MS Paint? See day13code.png


def coordsandfolds(contents):
    coords = set()
    folds = list()
    parsefolds = False
    for line in contents:
        if not parsefolds:
            if line != "":
                splitcoord = line.split(",")
                coords.add((int(splitcoord[0]), int(splitcoord[1])))
            else:
                parsefolds = True
        else:
            splitfold = line.split(" ")[2].split("=")
            folds.append((splitfold[0], int(splitfold[1])))
    return coords, folds


def fold(oldcoords, foldline):
    newcoords = set()
    for coord in oldcoords:
        if foldline[0] == "x":
            if coord[0] > foldline[1]:
                newcoords.add((foldline[1] * 2 - coord[0], coord[1]))
            else:
                newcoords.add(coord)
        elif foldline[0] == "y":
            if coord[1] > foldline[1]:
                newcoords.add((coord[0], foldline[1] * 2 - coord[1]))
            else:
                newcoords.add(coord)
    return newcoords


if __name__ == "__main__":
    part1("./data/day13part1.txt")
    part2("./data/day13part1.txt")
