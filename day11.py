# chr(ord(char) + 1)
# a = 97
# z = 122
import re
aVal,zVal = 97,122
#Part 1 input = hepxcrrq
#Part 2 input/part 1 answer = hepxxyzz
santasPass = "hepxxyzz"
check1,check2,check3,badpass = False,False,False,True
alphabet = "abcdefghijklmnopqrstuvwxyz"

while (badpass):
	#Increment String Logic Here
	for i in range(1,len(santasPass)+1):
		if(santasPass[-i] != 'z'):
			santasPass = list(santasPass)
			santasPass[-i] = chr(ord(santasPass[-i]) + 1)
			santasPass = "".join(santasPass)
			break
		else:
			santasPass = list(santasPass)
			santasPass[-i] = 'a'
			santasPass = "".join(santasPass)
	#Checks if there is a series of 3 letters in alphabetical order
	for i in range(len(alphabet)-2):
		if (alphabet[i:i+3] in santasPass):
			check1 = True
	#Checks if the password contains i, o, or l
	if ("i" not in santasPass or "o" not in santasPass or "l" not in santasPass):
		check2 = True
	#Checks if there are two pairs of identical letters
	match = re.match(R".*((\w)\2)(?!\2).*((\w)\4).*", santasPass)
	if (match != None):
		check3 = True
	if (check1 == True and check2 == True and check3 == True):
		badpass = False
	else:
		check1 = False
		check2 = False
		check3 = False
print (santasPass)

