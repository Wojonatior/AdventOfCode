import itertools
packages = []
packages = []
smallestFound = False

with open("day24input.txt", 'r') as f:
	for line in f:
		packages.append(int(line))

splitSize = sum(packages)/3
print(splitSize)
possible = []

largestPerm = 0

for i in range(len(packages)):
	print("Arrangments of size " + str(i))
	for perm in itertools.permutations(packages,i):
		permSum = sum(perm)
		largestPerm = max(largestPerm,permSum)
		print(largestPerm)
		if permSum == splitSize:
			smallestFound = True
			possible.append(perm)
	if(smallestFound):
		break
minQE = 9999999999
for arrangement in possible:
	QE = 1
	for package in arrangement:
		QE *= package
	minQE = min(minQE,QE)

print (minQE)