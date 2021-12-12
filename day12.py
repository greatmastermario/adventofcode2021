import adventutils


def part1(file):
    print("Part 1")
    inputs = adventutils.file_contents(file)
    routes = getroutes(inputs)
    fullpaths = traverse("start", "start", routes)
    # print(fullpaths)
    print(len(fullpaths))


def part2(file):
    print("Part 2")
    inputs = adventutils.file_contents(file)
    routes = getroutes(inputs)
    fullpaths = traverselong("start", "start", routes)
    # print(fullpaths)
    print(len(fullpaths))


def getroutes(inputs):
    routes = dict()
    for route in inputs:
        start, end = route.split("-")
        if start not in routes.keys():
            routes[start] = [end]
        else:
            routes[start].append(end)
        if end not in routes.keys():
            routes[end] = [start]
        else:
            routes[end].append(start)
    return routes


def traverse(path, laststop, routes):
    fullpaths = list()
    for nextstop in routes[laststop]:
        if (nextstop not in path or nextstop.isupper()) and nextstop != "end":
            fullpaths += traverse(path + "," + nextstop, nextstop, routes)
        elif nextstop == "end":
            fullpaths += [path + "," + nextstop]
    return fullpaths


def traverselong(path, laststop, routes):
    fullpaths = list()
    for nextstop in routes[laststop]:
        if (cantraverselong(path, nextstop)) and nextstop != "end":
            fullpaths += traverselong(path + "," + nextstop, nextstop, routes)
        elif nextstop == "end":
            fullpaths += [path + "," + nextstop]
    return fullpaths


def cantraverselong(path, nextstop):
    if nextstop not in path:
        return True
    if nextstop.isupper():
        return True
    if nextstop == "start":
        return False
    if nextstop in path:
        visitedsmall = dict()
        for stop in path.split(","):
            if stop.islower():
                if stop not in visitedsmall.keys():
                    visitedsmall[stop] = 1
                else:
                    visitedsmall[stop] += 1
        return 2 not in visitedsmall.values()
    return True


if __name__ == "__main__":
    part1("./data/day12part1.txt")
    part2("./data/day12part1.txt")
