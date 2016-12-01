import re,itertools

f = open("day9input.txt", "r")
translation = {}
distances = {}
translationCount = 0
allPaths = []

for line in f:
	regex = re.match(R"(\w+) to (\w+) = (\d+)", line)
	location1 = regex.group(1)
	location2 = regex.group(2)
	distance = regex.group(3)

	#Translate location names to numbers 
	index1 = translation.get(location1)
	if(index1 == None):
		translation[location1] = translationCount
		index1 = translationCount
		translationCount += 1
	index2 = translation.get(location2)
	if(index2 == None):
		translation[location2] = translationCount
		index2 = translationCount
		translationCount += 1

	#Save distances to the distance dict
	distances[str(index1)+str(index2)] = int(distance)
	distances[str(index2)+str(index1)] = int(distance)

#returns a list of lists 
perms = list(itertools.permutations(range(translationCount)))
#Iterates over each permutation
for permutation in perms:
	#Resets the current path cost
	pathCost = 0
	#Calculates past cost by summing the costs from each pair of locations
	for i in range(len(permutation)-1):
		j = i+1
		arg = str(permutation[i]) + str(permutation[j])
		pathCost += distances.get(arg)
	allPaths.append(pathCost)
print ("The shortest distance is " + str(min(allPaths)))
print ("The longest distance is " + str(max(allPaths)))