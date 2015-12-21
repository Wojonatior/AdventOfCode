# chr(ord(char) + 1)
# a = 97
# z = 122
import re
aVal,zVal = 97,122
santasPass = "hepxcrrq"
check1,check2,check3,badpass = False,False,False,True
alphabet = "abcdefghijklmnopqrstuvwxyz"

while (badpass):
	#Increment String Logic Here

	#Checks if there is a series of 3 letters in alphabetical order
	for i in range(len(alphabet)-2):
		if (alphabet[i:i+2] in santasPass):
			check1 = True
	#Checks if the password contains i, o, or l
	if ("i" not in santasPass or "o" not in santasPass or "l" not in santasPass):
		check2 = True
	#Checks if there are two pairs of identical letters
	match = re.match(R".*((\w)\2)(?!\2).*((\w)\4).*", santasPass)
	if (match != None):
		check3 = true
	if (check1 == True and check2 == True and check3 == True):
		badpass = False
print (santasPass)

def incrementString(target):
	count = len(taget) - 1
	unIncrmented = True
	while(unIncrmented):
		char = target[count]
		if(ord(char) > zVal):
			char = "a"
		else:
			unIncrmented = False
		target = target[:count] + chr(ord(char)) + target[i+1:]

characters = []
for i in range(len(santasPass)):
	characters.append( chr((((ord(santasPass[len(santasPass)-i-1]) + 1 * (ord(santasPass[len(santasPass)-i-1])-96 // 26 ** i))-97) % 26 )+ 97) )
#char7 = ord(c)-96 // 26 ** 1
#char6 = ord(c)-96 // 26 ** 2
#char5 = ord(c)-96 // 26 ** 3
#char4 = ord(c)-96 // 26 ** 4
#char3 = ord(c)-96 // 26 ** 5
#char2 = ord(c)-96 // 26 ** 6
#char1 = ord(c)-96 // 26 ** 7
