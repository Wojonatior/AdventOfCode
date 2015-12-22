import re

f = open("day14input.txt", "r")
reindeers,raceTime = [],2503
bestdist = 0

for line in f:
	match = re.match(R"(\w+) can fly (\d{1,3}) km\/s for (\d{1,3}) seconds, but then must rest for (\d{1,3}) seconds.", line)
	#(Name, Fly Speed, Fly Time, Rest Time)
	reindeers.append((match.group(1), match.group(2), match.group(3), match.group(4)))
count = 0
allDistVsTime, scores = [], []
for reindeer in reindeers:
	flying, dist = True, 0
	name,speed,fly,rest, = reindeer[0],int(reindeer[1]),int(reindeer[2]),int(reindeer[3])
	remainingTime = fly
	distVsTime = []
	for second in range(raceTime):
		if (flying):
			dist+= speed
		remainingTime -= 1
		if(remainingTime == 0):
			if(flying):
				remainingTime = rest
				flying = False
			else:
				remainingTime = fly
				flying = True
		distVsTime.append(dist)
	bestdist = max(bestdist,dist)
	allDistVsTime.append(distVsTime)
	scores.append(0)
	count += 1
for second in range(raceTime):
	currentBestDist = 0
	bestRacer = -1
	for racer in range(len(scores)-1):
		if (allDistVsTime[racer][second] > currentBestDist):
			bestRacer = racer
			currentBestDist = allDistVsTime[racer][second]
	scores[bestRacer] += 1
	print (scores)
print (scores)
print (bestdist)
