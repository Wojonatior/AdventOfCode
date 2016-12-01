myInput = "1321131112"
#Part 1 is 40 generations, and part 2 is 50 generations
generations = 50

for generation in range(generations):
	print("This is generation " + str(generation+1))
	currentNum = myInput[0]
	count = 1
	newInput = ""
	#Iterate over each character in the string
	for i in range(1,len(myInput)):
		#If it's the current number, add to the count
		if (myInput[i] == currentNum):
			count+= 1
		#Otherwise, Add the cound and the current number to the temp, and change the current number
		else:
			newInput += str(count) + currentNum
			currentNum = myInput[i]
			count = 1
	else:
		newInput += str(count) + currentNum
	#Replace the old string with the new one
	myInput = newInput
	print(myInput)
	print (len(myInput))