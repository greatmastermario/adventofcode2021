import sys

import adventutils


def part1(file):
    print("Part 1")
    hexstream = adventutils.file_contents(file)[0]
    binarystream = convertstream(hexstream)
    version, _, output = parsestream(binarystream)
    print(version)
    print("Part 2")
    print(output)


def convertstream(hexstream):
    outputstream = ""
    for char in hexstream:
        outputstream += format(int(char, 16), "b").zfill(4)
    return outputstream


def parsestream(packet):
    if "1" not in packet:
        return 0, len(packet)
    version = int(packet[:3], 2)
    operatortype = int(packet[3:6], 2)
    processed = 6
    if operatortype == 4:
        processing = True
        literalstring = ""
        while processing:
            prefix = packet[processed]
            if prefix == "0":
                processing = False
            literalstring += packet[processed + 1:processed + 5]
            # Insert literal usage if required
            processed += 5
        literal = int(literalstring, 2)
    else:
        lengthtype = packet[processed]
        processed += 1
        literals = list()
        if lengthtype == "0":
            bitlength = int(packet[processed:processed + 15], 2)
            processed += 15
            endpacket = bitlength + processed
            while processed < endpacket:
                subversion, subprocessed, subliteral = parsestream(packet[processed:endpacket])
                version += subversion
                processed += subprocessed
                literals.append(subliteral)
        elif lengthtype == "1":
            subpacketcount = int(packet[processed:processed + 11], 2)
            processed += 11
            for _ in range(subpacketcount):
                subversion, subprocessed, subliteral = parsestream(packet[processed:])
                version += subversion
                processed += subprocessed
                literals.append(subliteral)
        else:
            sys.exit(404)
        literal = operate(literals, operatortype)
    return version, processed, literal


def operate(literals, type):
    if type == 0:
        return sum(literals)
    elif type == 1:
        product = 1
        for literal in literals:
            product *= literal
        return product
    elif type == 2:
        return min(literals)
    elif type == 3:
        return max(literals)
    elif type == 5:
        return 1 if literals[0] > literals[1] else 0
    elif type == 6:
        return 1 if literals[0] < literals[1] else 0
    elif type == 7:
        return 1 if literals[0] == literals[1] else 0


if __name__ == "__main__":
    part1("./data/day16part1.txt")
