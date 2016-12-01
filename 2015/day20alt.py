n = 34000000
house = [0]*n
for i in range(1,int(n/10)):
	for j in range(i,min(i*50,int(n/10)),i):
		house[j] += i * 11
for i in range(n):
	if house[i] >= n:
		print (i)
		break