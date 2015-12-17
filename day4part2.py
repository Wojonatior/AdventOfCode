import hashlib,re
puzzleKey = "ckczppom"
hashNum = 0
found = False


while (not found):
	hashArg = puzzleKey + str(hashNum)
	hash_object = hashlib.md5(hashArg.encode())
	digest = hash_object.hexdigest()
	match = re.match(R"000000.*", digest)
	if (match != None):
		found = True
	else:
		hashNum += 1

print (hashNum)