instructions = []
# part 1 = [0,0]
# part 2 = [1,0]
regs = [1,0]
currentReg = -1
for line in open("day23input.txt", "r"):
	instructions.append(str(line))

i = 0
while i < len(instructions):
	#Reg a = 0, b = 1
	if 'a' in instructions[i]:
		currentReg = 0
	else:
		currentReg = 1

	if 'hlf' in instructions[i]:
		regs[currentReg] = regs[currentReg] // 2
		i += 1
	elif 'tpl' in instructions[i]:
		regs[currentReg] = regs[currentReg] * 3
		i += 1
	elif 'inc' in instructions[i]:
		regs[currentReg] = regs[currentReg] + 1
		i += 1
	elif 'jmp' in instructions[i]:
		offset = int(instructions[i][4:])
		i += offset
	elif 'jie' in instructions[i]:
		offset = int(instructions[i][7:])
		if((regs[currentReg] % 2) == 0):
			i += offset
		else:
			i += 1
	elif 'jio' in instructions[i]:
		offset = int(instructions[i][7:])
		if(regs[currentReg] == 1):
			i += offset
		else:
			i += 1

print("a:" + str(regs[0]))
print("b:" + str(regs[1]))