import adventutils


def part1(file):
    print("Part 1")
    xtarget, ytarget = targetcoords(adventutils.file_contents(file)[0])
    print(optimizedmaxy(ytarget))


def part2(file):
    print("Part 2")
    xtarget, ytarget = targetcoords(adventutils.file_contents(file)[0])
    print(counttrajectories(xtarget, ytarget))


def targetcoords(inputs):
    split = inputs.split(" ")
    splitx = split[2][2:-1].split("..")
    splity = split[3][2:].split("..")
    return (int(splitx[0]), int(splitx[1])), (int(splity[0]), int(splity[1]))


def optimizedmaxy(ytarget):
    ymax = 0
    startvelocity = 1
    while True:
        velocity = startvelocity
        tempymax = 0
        y = 0
        while y >= ytarget[0]:
            y += velocity
            velocity -= 1
            if velocity == 0:
                tempymax = y
            elif y in range(ytarget[0], ytarget[1] + 1):
                ymax = max(ymax, tempymax)
                break
        if velocity < ytarget[0]:
            break
        startvelocity += 1
    return ymax


def xmaps(xtarget):
    stepmap = dict()
    zerodropmap = dict()
    for startvelocity in range(1, xtarget[1] + 1):
        steps = 0
        x = 0
        velocity = startvelocity
        while x <= xtarget[1]:
            steps += 1
            x += velocity
            if x in range(xtarget[0], xtarget[1] + 1):
                if velocity > 1:
                    if steps in stepmap.keys():
                        stepmap[steps].append(startvelocity)
                    else:
                        stepmap[steps] = [startvelocity]
                if velocity == 1:
                    if steps + 1 in zerodropmap.keys():
                        zerodropmap[steps].append(startvelocity)
                    else:
                        zerodropmap[steps] = [startvelocity]
            if velocity == 1:
                break
            velocity -= 1
    return stepmap, zerodropmap


def counttrajectories(xtarget, ytarget):
    stepmap, zerodropmap = xmaps(xtarget)
    trajectories = set()
    startvelocity = ytarget[0]
    while True:
        velocity = startvelocity
        y = 0
        steps = 0
        added = False
        while y >= ytarget[0]:
            if y in range(ytarget[0], ytarget[1] + 1):
                if steps in stepmap.keys():
                    for x in stepmap[steps]:
                        trajectories.add((x, startvelocity))
                    added = True
                for step in zerodropmap.keys():
                    if steps >= step:
                        for x in zerodropmap[step]:
                            trajectories.add((x, startvelocity))
                        added = True
            y += velocity
            velocity -= 1
            steps += 1
        if not added and velocity < ytarget[0]:
            break
        startvelocity += 1
    return len(trajectories)


if __name__ == "__main__":
    part1("./data/day17part1.txt")
    part2("./data/day17part1.txt")
