import adventutils


def part1(file):
    print("Part 1")
    scanners = scannersandbeacons(adventutils.file_contents(file))
    constellation = getconstellation(scanners)
    count = 0
    for beacon in constellation:
        if not beacon.isscanner:
            count += 1
    print(count)
    print("Part 2")
    print(maxmanhattan(constellation))


def scannersandbeacons(inputs):
    scanners = list()
    for line in inputs:
        if "scanner" in line:
            beacons = list()
        elif "" == line:
            beacons.append(Beacon(0, 0, 0, True))
            beacons.sort()
            scanners.append(beacons)
            beacons = list()
        else:
            coords = line.split(",")
            beacons.append(Beacon(int(coords[0]), int(coords[1]), int(coords[2]), False))
    beacons.append(Beacon(0, 0, 0, True))
    beacons.sort()
    scanners.append(beacons)
    return scanners


class Beacon(object):
    
    def __init__(self, x, y, z, isscanner):
        self.location = (x, y, z)
        self.isscanner = isscanner

    def __eq__(self, other):
        return self.location == other.location and self.isscanner == other.isscanner

    def __gt__(self, other):
        return self.location > other.location

    def __lt__(self, other):
        return self.location < other.location

    def __hash__(self):
        return hash(self.location)


def orientations(beacons):
    orientationlist = list()
    orientationlist.append(beacons)
    orientationlist.append([Beacon(beacon.location[0], beacon.location[2], -beacon.location[1], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[0], -beacon.location[1], -beacon.location[2], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[0], -beacon.location[2], beacon.location[1], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[2], beacon.location[1], -beacon.location[0], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[2], -beacon.location[0], -beacon.location[1], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[2], -beacon.location[1], beacon.location[0], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[2], beacon.location[0], -beacon.location[1], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[0], beacon.location[2], beacon.location[1], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[0], beacon.location[1], -beacon.location[2], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[0], -beacon.location[2], -beacon.location[1], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[0], -beacon.location[1], beacon.location[2], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[2], beacon.location[1], beacon.location[0], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[2], beacon.location[0], -beacon.location[1], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[2], -beacon.location[1], -beacon.location[0], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[2], -beacon.location[0], beacon.location[1], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[1], -beacon.location[2], -beacon.location[0], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[1], beacon.location[0], -beacon.location[2], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[1], beacon.location[2], beacon.location[0], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(beacon.location[1], -beacon.location[0], beacon.location[2], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[1], -beacon.location[2], beacon.location[0], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[1], beacon.location[0], beacon.location[2], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[1], beacon.location[2], -beacon.location[0], beacon.isscanner)
                            for beacon in beacons])
    orientationlist.append([Beacon(-beacon.location[1], -beacon.location[0], -beacon.location[2], beacon.isscanner)
                            for beacon in beacons])
    for orientation in orientationlist:
        orientation.sort(key=lambda beacon: beacon.location)
    return orientationlist


def coorddiff(beacon1, beacon2):
    return beacon1[0] - beacon2[0], beacon1[1] - beacon2[1], beacon1[2] - beacon2[2]


def checkintersect(constellation, orientation):
    for index in range(len(constellation) - 11):
        constorigin = constellation[index].location
        constdiff = [coorddiff(constorigin, constpoint.location) for constpoint in constellation]
        for orientindex in range(len(orientation) - 11):
            orientorigin = orientation[orientindex].location
            orientdiff = [coorddiff(orientorigin, orientpoint.location) for orientpoint in orientation]
            if len(set(constdiff).intersection(set(orientdiff))) >= 12:  # 12 beacons + 1 scanner
                return True, coorddiff(constorigin, orientorigin)
    return False, None


def getconstellation(scanners):
    while len(scanners) > 1:
        beaconstoremove = None
        for beacons in scanners:
            isintersected = False
            for otherbeacons in scanners:
                if otherbeacons == beacons:
                    continue
                for orientation in orientations(otherbeacons):
                    isintersected, diff = checkintersect(beacons, orientation)
                    if isintersected:
                        print("Found intersect")
                        scanners.append(list(set(beacons)
                                             .union(set([Beacon(beacon.location[0] + diff[0],
                                                                beacon.location[1] + diff[1],
                                                                beacon.location[2] + diff[2], beacon.isscanner)
                                                         for beacon in orientation]))))
                        beaconstoremove = [otherbeacons, beacons]
                        break
                if isintersected:
                    break
            if isintersected:
                break
        if beaconstoremove is not None:
            for beaconlist in beaconstoremove:
                scanners.remove(beaconlist)
        else:
            print("No beacons match found")
    return scanners[0]


def maxmanhattan(beacons):
    distance = 0
    scanners = list()
    for beacon in beacons:
        if beacon.isscanner:
            scanners.append(beacon)
    for index1 in range(len(scanners) - 1):
        for index2 in range(index1 + 1, len(scanners)):
            distance = max(distance, manhattandistance(scanners[index1], scanners[index2]))
    return distance


def manhattandistance(scanner1, scanner2):
    return abs(scanner1.location[0] - scanner2.location[0]) + abs(scanner1.location[1] - scanner2.location[1]) +\
           abs(scanner1.location[2] - scanner2.location[2])


if __name__ == "__main__":
    part1("./data/day19part1.txt")
