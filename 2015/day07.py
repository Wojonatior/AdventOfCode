import re

circuit = {}
circuit['1'] = 1
circuit['b'] = 3176
operations = []

f = open('day7input.txt', 'r')

def assignFunc (operand1, operand2, target):
	signal1 = circuit.get(operand1)
	signal2 = None
	if (signal1 == None):
		return False
	circuit[target] = signal1
	return True

def notFunc (operand1, operand2, target):
	signal1 = circuit.get(operand1)
	signal2 = None
	if (signal1 == None):
		return False
	circuit[target] = ~signal1
	return True

def andFunc (operand1, operand2, target):
	signal1 = circuit.get(operand1)
	signal2 = circuit.get(operand2)
	if (signal1 == None or signal2 == None):
		return False
	circuit[target] = signal1 & signal2
	return True

def orFunc (operand1, operand2, target):
	signal1 = circuit.get(operand1)
	signal2 = circuit.get(operand2)
	if (signal1 == None or signal2 == None):
		return False
	circuit[target] = signal1 | signal2
	return True

def lshiftFunc (operand1, operand2, target):
	signal1 = circuit.get(operand1)
	signal2 = int(operand2)
	if (signal1 == None):
		return False
	circuit[target] = signal1 << signal2
	return True

def rshiftFunc (operand1, operand2, target):
	signal1 = circuit.get(operand1)
	signal2 = int(operand2)
	if (signal1 == None):
		return False
	circuit[target] = signal1 >> signal2
	return True

for line in f:
	isNot = False
	isAssignment = False

	#Parsing
	parsed = re.match(R'^(\w+) -> (\w{1,2})', line)
	if (parsed != None):
		# If the operand consists of numbers, assign the circuit value
		if (re.match(R'^(\d+) -> (\w{1,2})', line) != None):
			if(parsed.group(2)!="b"):
				circuit[parsed.group(2)] = min(int(parsed.group(1)),65535)
				print("Value Set")
			continue
		#Otherwise, assign it later
		isAssignment = True
	elif ('NOT' in line):
		parsed = re.match(R'(NOT) (\w{1,2}) -> (\w{1,2})', line)
		isNot  = True
	elif ('AND' in line):
		parsed = re.match(R'(\w{1,2}) (AND) (\w{1,2}) -> (\w{1,2})', line)
	elif ('OR' in line):
		parsed = re.match(R'(\w{1,2}) (OR) (\w{1,2}) -> (\w{1,2})', line)
	elif ('LSHIFT' in line):
		parsed = re.match(R'(\w{1,2}) (LSHIFT) (\w{1,2}) -> (\w{1,2})', line)
	elif ('RSHIFT' in line):
		parsed = re.match(R'(\w{1,2}) (RSHIFT) (\w{1,2}) -> (\w{1,2})', line)

	#Storage
	if(isAssignment):
		#(ASSIGN, Operand1, dud value, target)
		operations.append(("ASSIGN",parsed.group(1),None,parsed.group(2)))
		print("Command Added")
	elif(isNot):
		# (NOT, Operand1, dud value, target)
		operations.append((parsed.group(1),parsed.group(2),None,parsed.group(3)))
		print("Command Added")
	else:
		# (Operator, Operand1, Operand2, target)
		operations.append((parsed.group(2),parsed.group(1),parsed.group(3),parsed.group(4)))
		print("Command Added ")

while(len(operations) > 0):
	#Iterate over all operations
	for operation in operations:
		#Check Operator type
		print (operation[0])
		if (operation[0] == 'NOT'):
			operatorFunction = notFunc
		elif (operation[0] == 'ASSIGN'):
			operatorFunction = assignFunc
		elif (operation[0] == 'AND'):
			operatorFunction = andFunc
		elif (operation[0] == 'OR'):
			operatorFunction = orFunc
		elif (operation[0] == 'RSHIFT'):
			operatorFunction = rshiftFunc
		elif (operation[0] == 'LSHIFT'):
			operatorFunction = lshiftFunc
		else:
			print ("Something fell through")
		#Calculate Result/Check if operation can be performed
		successful = operatorFunction(operation[1],operation[2],operation[3])
		print (successful)
		#Remove successful operation
		if(successful):
			operations.remove(operation)
			print (int(len(operations)))


print ("The signal at a is " + str(circuit.get("a")))