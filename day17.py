import itertools

eggnog, sizes, combinations = 150,[],0
minFound = False

for line in open("day17input.txt"):
	sizes.append(int(line))
for i in range(len(sizes)):
	for comb in itertools.combinations(sizes, i):
		if sum(comb) == 150:
			combinations += 1
			minFound = True
	if minFound:
		break
print (combinations)

