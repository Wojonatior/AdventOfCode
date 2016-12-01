import re

f = open('day5input.txt', 'r')
badWords, goodWords = [],[]

for line in f:
	word = str(line)
	#If there aren't 3 vowels, word is naughty
	check1 = re.match(R'.*[aeiou].*[aeiou].*[aeiou].*', word)
	#If there isn't a repeated 2 chars, word is naughty
	check2 = re.match(R'.*(\w)\1.*', word)
	#If there is a forbidden substring, word is naughty
	check3 = re.match(R'.*(ab|cd|pq|xy).*', word)

	if (check1 == None || check2 == None || check3 != None):
		badWords.append(word)
	else:
		goodWords.append(word)

print("There are " +  str(len(badWords)) + " naughty words and " +  str(len(goodWords)) + " Nice words")