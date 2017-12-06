### Step 1 ### 
with open('5.input', 'r') as f:
	instructions = f.readlines()
instructions = [int(i.strip()) for i in instructions]
orig_instructions = instructions

IP = 0
total = 0
while True:
	try:
		instruction = instructions[IP]
		total += 1
		instructions[IP] += 1
		IP += instruction
	except:
		print "step1: "+str(total)
		break

### Step 2 ###
with open('5.input', 'r') as f:
	instructions = f.readlines()
instructions = [int(i.strip()) for i in instructions]

IP = 0
total = 0
while True:
	try:
		instruction = instructions[IP]
		total += 1
		instructions[IP] += [-1 if instruction>=3 else 1][0]
		IP += instruction
	except:
		print "step2: "+str(total)
		break



