instructions = open('day1input', 'r').read()

floor,firstBasementFloor = 0,-1
for i in range(len(instructions)):
	if(instructions[i] == R"("):
		floor += 1
	if(instructions[i] == R")"):
		floor -= 1
	if(floor < 0 and firstBasementFloor == -1):
		firstBasementFloor = i + 1
print("Santa is on floor " + str(floor))
print("Santa is on floor " + str(firstBasementFloor))