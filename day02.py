import re
totalPaper = 0
totalRibbon = 0
f = open('day2input.txt', 'r')
for line in f:
	match = re.match(R"(\d+)x(\d+)x(\d+)", line)
	length = int(match.group(1))
	width = int(match.group(2))
	height = int(match.group(3))

	cubicSize = length * width * height

	side1 = length * width
	side1p = length*2 + width*2

	side2 = length * height
	side2p = length*2 + height*2

	side3 = width * height
	side3p = width*2 + height*2

	smallestSide = min(side1,side2,side3)
	smallestPerim = min(side1p,side2p,side3p)

	totalRibbon += smallestPerim + cubicSize
	totalPaper += smallestSide + side1*2 + side2*2 + side3*2
print(str(totalPaper) + " " + str(totalRibbon))
