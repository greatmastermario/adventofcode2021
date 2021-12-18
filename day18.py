import adventutils
import math


def part1(file):
    print("Part 1")
    snailnums = adventutils.file_contents(file)
    result = None
    for index, snailnum in enumerate(snailnums):
        print("Adding snailnum", index)
        num = Pair(pairstring=snailnum)
        if result is None:
            result = num
        else:
            result += num
            result.simplify()
    print("Getting magnitude")
    print(result.magnitude())


def part2(file):
    print("Part 2")
    snailnums = adventutils.file_contents(file)
    maxmag = 0
    for firstindex, snailnum1 in enumerate(snailnums):
        for secondindex, snailnum2 in enumerate(snailnums):
            if firstindex != secondindex:
                total = Pair(pairstring=snailnum1) + Pair(pairstring=snailnum2)
                total.simplify()
                maxmag = max(maxmag, total.magnitude())
    print(maxmag)


class Pair(object):
    def __init__(self, **kwargs):
        if "pairstring" in kwargs.keys():
            pairstring = kwargs["pairstring"]
            brackets = 0
            for index, char in enumerate(pairstring):
                if char == "," and brackets == 1:
                    self.left = int(pairstring[1]) if index == 2 else Pair(pairstring=pairstring[1:index])
                    self.right = int(pairstring[-2]) if index == len(pairstring) - 3 else \
                        Pair(pairstring=pairstring[index + 1:-1])
                    break
                elif char == "[":
                    brackets += 1
                elif char == "]":
                    brackets -= 1
        else:
            self.left = kwargs["left"]
            self.right = kwargs["right"]

    def __add__(self, other):
        return Pair(left=self, right=other)

    def __str__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]"

    def simplify(self):
        while self.explode(1)[0] or self.split():
            pass

    def explode(self, depth):
        if type(self.left) == Pair:
            exploded, explodeleft, exploderight = self.left.explode(depth + 1)
            if exploderight is not None:
                if type(self.right) == Pair:
                    self.right.addleft(exploderight)
                else:
                    self.right += exploderight
            if explodeleft is not None and exploderight is not None:
                self.left = 0
            if exploded:
                return exploded, explodeleft, None
        if type(self.right) == Pair:
            exploded, explodeleft, exploderight = self.right.explode(depth + 1)
            if explodeleft is not None:
                if type(self.left) == Pair:
                    self.left.addright(explodeleft)
                else:
                    self.left += explodeleft
            if explodeleft is not None and exploderight is not None:
                self.right = 0
            if exploded:
                return exploded, None, exploderight
        if type(self.left) == int and type(self.right) == int and depth >= 5:
            return True, self.left, self.right
        return False, None, None

    def addleft(self, val):
        if type(self.left) == Pair:
            self.left.addleft(val)
        else:
            self.left += val

    def addright(self, val):
        if type(self.right) == Pair:
            self.right.addright(val)
        else:
            self.right += val

    def split(self):
        if type(self.left) == Pair:
            if self.left.split():
                return True
        elif self.left > 9:
            self.left = Pair(left=math.floor(self.left / 2), right=math.ceil(self.left / 2))
            return True
        if type(self.right) == Pair:
            if self.right.split():
                return True
        elif self.right > 9:
            self.right = Pair(left=math.floor(self.right / 2), right=math.ceil(self.right / 2))
            return True
        return False

    def magnitude(self):
        if type(self.left) == Pair:
            magleft = self.left.magnitude()
        else:
            magleft = self.left
        if type(self.right) == Pair:
            magright = self.right.magnitude()
        else:
            magright = self.right
        return 3 * magleft + 2 * magright


if __name__ == "__main__":
    part1("./data/day18part1.txt")
    part2("./data/day18part1.txt")
