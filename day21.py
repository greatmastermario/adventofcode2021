import adventutils


def part1(file):
    print("Part 1")
    playerspaces = getplayerspaces(adventutils.file_contents(file))
    playerscores, rollcount = play(playerspaces)
    print(min(playerscores) * rollcount)


def part2(file):
    print("Part 2")
    players = getquantumplayers(adventutils.file_contents(file))
    wins = playquantum(players)
    print(max(wins))


class DeterministicDie(object):
    def __init__(self):
        self.val = 1

    def roll(self):
        rollval = self.val
        self.val = self.val + 1 if self.val < 100 else 1
        return rollval


def play(playerspaces):
    die = DeterministicDie()
    rollcount = 0
    playerscores = [0 for _ in playerspaces.keys()]
    turn = 0
    while not checkscores(playerscores):
        move = die.roll() + die.roll() + die.roll()
        space = playerspaces[turn] + move
        while space > 10:
            space -= 10
        playerspaces[turn] = space
        playerscores[turn] += space
        rollcount += 3
        turn = turn + 1 if turn < len(playerspaces) - 1 else 0
    return playerscores, rollcount


def checkscores(playerscores):
    for score in playerscores:
        if score >= 1000:
            return True
    return False


def getplayerspaces(contents):
    playerspaces = dict()
    for index, line in enumerate(contents):
        playerspaces[index] = int(line.split(" ")[-1])
    return playerspaces


def addspacescores(newspacescores, spacescore, count, increment, incrementcount):
    newspace = spacescore[0] + increment
    if newspace > 10:
        newspace -= 10
    newkey = (newspace, spacescore[1] + newspace)
    if newkey in newspacescores:
        newspacescores[newkey] += count * incrementcount
    else:
        newspacescores[newkey] = count * incrementcount


class QuantumPlayer(object):
    def __init__(self, startingspace):
        self.spacescores = {(startingspace, 0): 1}  # Space -> Score -> Count

    def move(self):
        newspacescores = dict()
        for spacescore, count in self.spacescores.items():
            addspacescores(newspacescores, spacescore, count, 3, 1)
            addspacescores(newspacescores, spacescore, count, 4, 3)
            addspacescores(newspacescores, spacescore, count, 5, 6)
            addspacescores(newspacescores, spacescore, count, 6, 7)
            addspacescores(newspacescores, spacescore, count, 7, 6)
            addspacescores(newspacescores, spacescore, count, 8, 3)
            addspacescores(newspacescores, spacescore, count, 9, 1)
        self.spacescores = newspacescores

    def getwins(self):
        wins = 0
        keystoremove = list()
        for spacescore, count in self.spacescores.items():
            if spacescore[1] >= 21:
                wins += count
                keystoremove.append(spacescore)
        for key in keystoremove:
            self.spacescores.__delitem__(key)
        return wins

    def getgamecount(self):
        count = 0
        for spacecount in self.spacescores.values():
            count += spacecount
        return count


def playquantum(players):
    playerwins = [0 for _ in players]
    turn = 0
    while not quantumgameover(players):
        players[turn].move()
        playerwins[turn] += players[turn].getwins() * sum([player.getgamecount() for player in players
                                                           if player != players[turn]])
        turn = turn + 1 if turn < len(players) - 1 else 0
    return playerwins


def quantumgameover(players):
    for player in players:
        if len(player.spacescores) == 0:
            return True
    return False


def getquantumplayers(contents):
    players = list()
    for line in contents:
        players.append(QuantumPlayer(int(line.split(" ")[-1])))
    return players


if __name__ == "__main__":
    part1("./data/day21part1.txt")
    part2("./data/day21part1.txt")
