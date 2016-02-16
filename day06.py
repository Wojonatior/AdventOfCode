import re

lightGrid = [[False for x in range(1000)] for x in range(1000)]
lightsOn = 0

f = open('day6input.txt', 'r')

def toggle(x,y):
	lightGrid[x][y] = not lightGrid[x][y]
def turn_on(x,y):
	lightGrid[x][y] = True
def turn_off(x,y):
	lightGrid[x][y] = False

for line in f:
	command = str(line)
	command = re.match(R'(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)', command)
	start_x, start_y, end_x, end_y = int(command.group(2)),int(command.group(3)),int(command.group(4)),int(command.group(5))
	command_type = command.group(1)
	if (command_type == "toggle"):
		command_call = toggle
	elif (command_type == "turn on"):
		command_call = turn_on
	else:
		command_call = turn_off
	for x in range(start_x,end_x+1):
		for y in range(start_y,end_y+1):
			command_call(x,y)

	
for x in range(1000):
		for y in range(1000):
			if (lightGrid[x][y]):
				lightsOn += 1
print (str(lightsOn))