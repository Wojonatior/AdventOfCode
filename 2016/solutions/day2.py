with open("../input/day2input.txt") as f:
    puzzleinput = f.read()

keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]
t = True
f = False
validLocations = [[f,f,f,f,f],
                  [f,t,t,t,f],
                  [f,t,t,t,f],
                  [f,t,t,t,f],
                  [f,f,f,f,f],]
finalAnswer = []
currentCoords = [2,2]

def checkMove(dir, coords):
    directionDict = {
        "U":(1,0),
        "D":(-1,0),
        "R":(0,1),
        "L":(0,-1)
    }
    y,x = directionDict[dir]
    newCoords = (coords[0]+y, coords[1]+x)
    return (newCoords, validLocations[newCoords[0]][newCoords[1]])

#remember to adjust the indicies when checking "valid locations"
for instruction in puzzleinput:
    directionList = list(instruction) 
    for direction in directionList:
       (newMove, validMove) = checkMove(direction, currentCoords)
       if validMove:
           currentCoords = newMove
    finalAnswer.append(str(
        keypad[ currentCoords[0] ][ currentCoords[1] ] ))

print(finalAnswer)

