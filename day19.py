import re

calibration = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
#calibration = "HOH"
replacements = []
#replacements = [("H", "HO"),("H", "OH"),("O", "HH")]
resultingMolecules = {}
moleculeCount = 0

for line in open("day19input.txt", "r"):
	match = re.match(R"(\w+) => (\w+)", line)
	replacements.append((str(match.group(1)),str(match.group(2))))

for replacement in replacements:
	for i in range(len(calibration)-len(replacement[0])+1):
		if(calibration[i:i+len(replacement[0])] == replacement[0]):
			firstHalf = calibration[:i]
			secondHalf = calibration[i+len(replacement[0]):]
			middle = replacement[1]
			resultingMolecules[firstHalf + middle + secondHalf] = 1

print (len(resultingMolecules.items()))