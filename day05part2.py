import re

f = open('day5input.txt', 'r')
badWords, goodWords = [],[]

for line in f:
	word = str(line)
	#Two identical letters seperatex by exactly one letter
	check1 = re.match(R'.*(\w)\w\1.*', word)
	#2 character substring that repeats, but doesn't overlap
	check2 = re.match(R'.*(\w{2})(?:(?!\1).)*\1.*', word)

	if (check1 == None or check2 == None):
		badWords.append(word)
	else:
		goodWords.append(word)

print("There are " +  str(len(badWords)) + " naughty words and " +  str(len(goodWords)) + " Nice words")