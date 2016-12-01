f = open('day8input.txt', 'r')
sum1,sum2 = 0,0
for line in f:
	#Calculate the length of the line minus the newline character
	sum1 += len(line[:-1])
	#Calculate the length of the line as if it was evaluated in python
	sum2 += len(eval(line))
print (sum1-sum2+1)
