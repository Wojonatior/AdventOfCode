f = open('day8input.txt', 'r')

sum1,sum2 = 0,0

for line in f:
	#Check each char
	for i in range(len(line)-1):
		char = line[i]
		#If it needs to be escaped, add 1 to the count for the backslash
		if (char == "\"" or line[i] == "\\" or line[i] == ""):
			sum1 += 1
	#Add the contents of the line + 2, one for a double quote at each end
	sum1 += len(line[:-1]) + 2
	#Counting of the number of chars in each line minus the newline char
	sum2 += len(line[:-1])


#To compensate for the trimming of an extra character on the last line
sum2 -= 1

print (sum1 - sum2)