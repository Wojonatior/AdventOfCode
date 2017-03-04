import re
from collections import defaultdict

with open('../input/day4input.txt') as f:
    rooms = [ line.replace("-", "") for line in f.readlines()]

roomIdSum = 0

def buildDict(roomName):
    charDict = defaultdict(int)
    for char in roomName:
        charDict[char] += 1
    return charDict

def buildChecksum(charDict):
    fiveSortedChars = sorted(charDict.items(), key=lambda x: (x[1], - ord(x[0])), reverse=True)[:5]
    return "".join([charCount[0] for charCount in list(fiveSortedChars)])


for room in rooms:
    roomMatch = re.match("(\w*?)(\d{3})\[(\w{5})\]", room)
    roomName, id, checksum = (roomMatch.group(1), int(roomMatch.group(2)), roomMatch.group(3))
    charDict = buildDict(roomName)

    if buildChecksum(charDict) == checksum:
        print(id)
        roomIdSum += id

print(roomIdSum)
