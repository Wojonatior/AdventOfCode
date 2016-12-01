import time
santasPass = "abcdefgh"
print(santasPass)
while(True):
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
	print(santasPass)
	time.sleep(1)