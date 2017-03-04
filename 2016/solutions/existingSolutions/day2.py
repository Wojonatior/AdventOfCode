with open("../input/day2input.txt") as f:
    puzzleinput = f.read()

t = True
f = False
""" pt1 keypad
currentCoords = [1,1]
validLocations = [[f,f,f,f,f],
                  [f,t,t,t,f],
                  [f,t,t,t,f],
                  [f,t,t,t,f],
                  [f,f,f,f,f],]
keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]
"""
"pt2 keypad"
currentCoords = [3,0]
keypad = [[0, 0,  1,  0, 0],
          [0, 2,  3,  4, 0],
          [5, 6,  7,  8, 9],
          [0,"A","B","C",0],
          [0, 0, "D",0,  0],]
validLocations = [[f,f,f,f,f,f,f],
                  [f,f,f,t,f,f,f],
                  [f,f,t,t,t,f,f],
                  [f,t,t,t,t,t,f],
                  [f,f,t,t,t,f,f],
                  [f,f,f,t,f,f,f],
                  [f,f,f,f,f,f,f],]

finalAnswer = []
directionDict = {
    "D":(1,0),
    "U":(-1,0),
    "R":(0,1),
    "L":(0,-1)
}

def checkMove(dir, coords):
    y,x = directionDict[dir]
    newCoords = (coords[0]+y, coords[1]+x)
    return (newCoords, validLocations[newCoords[0]+1][newCoords[1]+1])

#remember to adjust the indicies when checking "valid locations"
for direction in puzzleinput:
    if direction == "\n":
        finalAnswer.append(str(keypad[ currentCoords[0] ][ currentCoords[1] ]))
    else:
        (newMove, validMove) = checkMove(direction, currentCoords)
        if validMove:
            currentCoords = newMove

print(str(finalAnswer))
