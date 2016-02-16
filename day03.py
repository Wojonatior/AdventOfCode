x,y = 0,0
robo_x, robo_y = 0,0
grid = {}
trueSanta = True
grid[str(x) + " "+ str(y)] = 1

f = open('day3input.txt', 'r')
instructions = str(f.read())

for instruction in instructions:

	if (instruction == '^'):
		if (trueSanta):
			y += 1
		else:
			robo_y += 1
	elif (instruction == 'v'):
		if (trueSanta):
			y -= 1
		else:
			robo_y -= 1
	elif (instruction == '<'):
		if (trueSanta):
			x -= 1
		else:
			robo_x -= 1
	elif (instruction == '>'):
		if (trueSanta):
			x += 1
		else:
			robo_x += 1

	if (trueSanta):
		cordinates = str(x) + " "+ str(y)
	else:
		cordinates = str(robo_x) + " "+ str(robo_y)

	current = grid.get(cordinates, None)

	if (current == None):
		grid[cordinates] = 1
	else:
		grid[cordinates] += 1

	trueSanta = not trueSanta

count = len(grid.items())
print ("There were " + str(count) + " distinct houses visited")