import re

f = open("day14input.txt", "r")
reindeers,raceTime = [],2503
bestdist = 0
allDistVsTime, scores = [], []

for line in f:
	match = re.match(R"(\w+) can fly (\d{1,3}) km\/s for (\d{1,3}) seconds, but then must rest for (\d{1,3}) seconds.", line)
	#(Name, Fly Speed, Fly Time, Rest Time)
	reindeers.append((match.group(1), match.group(2), match.group(3), match.group(4)))


for reindeer in reindeers:

	#Set the reindeer's stats
	name,speed,fly,rest, = reindeer[0],int(reindeer[1]),int(reindeer[2]),int(reindeer[3])
	#Start flying, at a distance of 0, and set the remaining fly time.
	flying, dist, remainingTime = True, 0, fly
	#Start a new dist vs. time list
	distVsTime = []

	for second in range(raceTime):
		#If Flying, increment distance
		if (flying):
			dist+= speed
		#Subtract 1 second from the remaining time on the current activity
		remainingTime -= 1
		#If there is no more time remaining on the current activity
		if(remainingTime == 0):
			#Set the rest time, and stop flying
			if(flying):
				remainingTime = rest
				flying = False
			#Otherwise, set the fly time and start flying
			else:
				remainingTime = fly
				flying = True
		#Append the current distance to the current distance list
		distVsTime.append(dist)
	#Keep track of the best final distance
	bestdist = max(bestdist,dist)
	#Add the list of distances for this reindeer to the list that holds all of the reindeer's informaiton
	allDistVsTime.append(distVsTime)
	#Add an empty score that corresponds to this racer
	scores.append(0)

for second in range(raceTime):

	currentBestDist = 0
	bestRacers = []

	for racer in range(len(scores)):

		if (allDistVsTime[racer][second] == currentBestDist):
			bestRacers.append(racer)
			currentBestDist = allDistVsTime[racer][second]
		elif (allDistVsTime[racer][second] > currentBestDist):
			bestRacers = [racer]
			currentBestDist = allDistVsTime[racer][second]

	for i in range(len(bestRacers)):
		print ("Best racers are: " + str(bestRacers))
		#i goes from 0-0 or 0-2 maybe
		#bestRacers[i] = Returns the index of a racer
		#Scores[index] = total score of racer at index i
		scores[bestRacers[i]] += 1

	print (scores)

print (list(range(len(scores))))
print (bestdist)