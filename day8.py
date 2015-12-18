f = open('day8input.txt', 'r')
sum1,sum2 = 0,0
for line in f:
	sum1 += len(line[:-1])
	sum2 += len(eval(line))
print (sum1-sum2+1)