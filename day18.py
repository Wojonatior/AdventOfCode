from copy import deepcopy 
lightGrid = [[False for z in range(103)] for z in range(103)]
y,generations = 1,100
count = 0

for line in open("day18input.txt" ,"r"):
	line =line.strip()
	for x in range(len(str(line))):
		if line[x] == '#':
			count += 1
			lightGrid[x+1][y] = True
	y += 1

lightGrid[1][1] = True
lightGrid[100][1] = True
lightGrid[1][100] = True
lightGrid[100][100] = True

for gen in range(generations):

	print("This is generation " + str(gen+1))

	#Assign the current state of the light grid to the tmporary grid
	tempLightGrid = deepcopy(lightGrid)#[[False for t in range(103)] for t in range(103)]

	for x2 in range(1,101):
		for y2 in range(1,101):

			adjacentOn = 0

			#check the state of the origional grid
			if(True):
				#8
				if(lightGrid[x2+1][y2+1]):
					adjacentOn += 1
				#5
				if(lightGrid[x2+1][y2]):
					adjacentOn += 1
				#3
				if(lightGrid[x2+1][y2-1]):
					adjacentOn += 1
				#6
				if(lightGrid[x2-1][y2+1]):
					adjacentOn += 1
				#4
				if(lightGrid[x2-1][y2]):
					adjacentOn += 1
				#1
				if(lightGrid[x2-1][y2-1]):
					adjacentOn += 1
				#2
				if(lightGrid[x2][y2+1]):
					adjacentOn += 1
				#7
				if(lightGrid[x2][y2-1]):
					adjacentOn += 1

			#make modifications to the new grid
			#If the light is on
			if(lightGrid[x2][y2]):
				if(adjacentOn == 2 or adjacentOn == 3):
					print("Light Kept On")
					tempLightGrid[x2][y2] = True
				else:
					print("Light Turned Off")
					tempLightGrid[x2][y2] = False
			#If the light is off and it has 3 on neighbors
			elif(adjacentOn == 3):
				print("Light Turned On")
				tempLightGrid[x2][y2] = True
	#Changes from new grid sent to origional 
	lightGrid = deepcopy(tempLightGrid)
	#For Part 2
	lightGrid[1][1] = True
	lightGrid[100][1] = True
	lightGrid[1][100] = True
	lightGrid[100][100] = True
			
	tempLightGrid = None

count = 0
for xx in range(1,101):
	for yy in range(1,101):
		if(lightGrid[xx][yy]):
			count += 1

print (count)