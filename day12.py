totalSum = 0
f = open("day12input.txt", "r")
textDump = f.readline()
value = ""
for i in range(len(textDump)):
	if(textDump[i].isdigit() or (textDump[i] == "-"and len(value)==0)):
			value += textDump[i]
	elif(len(value) != 0):
		totalSum += int(value)
		value = ""

print(totalSum)