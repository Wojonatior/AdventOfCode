import math
#34,000,000
minPresents,currentPresents = 34000000,0
house,bestPresents = 1,0
found, above = False, False

while (not found):
	house += 1
	factors = []
	for i in range(1,math.floor(math.sqrt(house)) +1):
		if(house % i == 0):
			factors.append(i)
	currentPresents = 10 * sum(factors)
	bestPresents = max(bestPresents,currentPresents)
	print ("House #" + str(house) + " With " + str(bestPresents) + "presents")
print (house)