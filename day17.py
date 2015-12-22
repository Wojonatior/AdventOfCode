import itertools

eggnog, sizes,combinations = 150,[],0

for line in open("day17input.txt"):
	sizes.append(int(line))

for perm in itertools.permutations(sizes):
	print (perm)
	for i in range(len(perm)-1):
		capacity = sum(perm[:(-i+1)])
		print(capacity)
		if (capacity == eggnog):
			combinations += 1
		if (capacity < eggnog):
			break

print (combinations)