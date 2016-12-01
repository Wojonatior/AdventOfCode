import re,itertools

f = open("day13input.txt", "r")
translation = {}
relations, bestTotal, count = {}, 0, 0

#Data processing
for line in f:
	match = re.match(R"(\w+) would (lose|gain) (\d{1,3}) happiness units by sitting next to (\w+)\.", line)

	#Lookup and create, if neccesary, translations from name -> index
	index1,index2 = translation.get(match.group(1)), translation.get(match.group(4))
	if(index1 == None):
		translation[match.group(1)] = count
		index1 = count
		count += 1
	if(index2 == None):
		translation[match.group(4)] = count
		index2 = count
		count += 1

	#Populate relationship "matrix"
	if(match.group(2) == "lose"):
		relations[str(index1)+str(index2)] = int("-" + match.group(3))
	else:
		relations[str(index1)+str(index2)] = int(match.group(3))

#Part 2
#0,1,2,3,4,5,6,7
for i in range(count):
	relations[str(i)+str(count)] = 0
	relations[str(count)+str(i)] = 0
count += 1

for permutation in itertools.permutations(range(count)):
	#Reset total to 0
	currentTotal = 0
	#Create key for lookup in dict
	key = str(permutation[0])+str(permutation[len(permutation)-1])
	#Lookup key, and key in reverse, in dict, and add to total
	currentTotal += relations.get(key)
	currentTotal += relations.get(key[::-1])

	for i in range(len(permutation)-1):
		#Create key for lookup in dict
		key = str(permutation[i])+str(permutation[i+1])
		print(key)
		#Lookup key, and key in reverse, in dict, and add to total
		currentTotal += relations.get(key)
		currentTotal += relations.get(key[::-1])
	#Assign the largest value of bestTotal and currentTotal to bestTotal
	bestTotal = max(bestTotal,currentTotal)

print(bestTotal)