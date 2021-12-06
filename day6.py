import adventutils
import collections


def part1(file):
    print("Part 1")
    fishlist = adventutils.file_contents(file)
    fishqueue = getfishdeque(fishlist)
    print(simfish(fishqueue, 80))


def part2(file):
    print("Part 2")
    fishlist = adventutils.file_contents(file)
    fishqueue = getfishdeque(fishlist)
    print(simfish(fishqueue, 256))


def simfish(fishqueue, time):
    for counter in range(time):
        breedcount = fishqueue.popleft()
        fishqueue[6] += breedcount
        fishqueue.append(breedcount)
    total = 0
    for fishcount in fishqueue:
        total += fishcount
    return total

def getfishdeque(fishlist):
    fishints = [int(fish) for fish in fishlist[0].split(",")]
    fishqueue = collections.deque()
    for index in range(9):
        fishqueue.append(0)
    for fishage in fishints:
        fishqueue[fishage] += 1
    return fishqueue


if __name__ == "__main__":
    part1("./data/day6part1.txt")
    part2("./data/day6part1.txt")
