buckets = '''14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'''.split("\t")
#buckets = '''0	2	7	0'''.split("\t")
buckets = [int(i) for i in buckets]

total = 0
seen = {}

while True:
	current_highest = 0
	current_highest_number = 0

	key = '|'.join([str(k) for k in buckets])
	#print key 
	if key in seen:
		print "step1: "+str(total)
		print "step2: "+str(total-seen[key]+1)
		exit()
	total += 1
	seen[key] = total

	for i in range(0, len(buckets)): #Find highest bucket
		bucket = buckets[i]
		if bucket > current_highest_number:
			current_highest = i
			current_highest_number = buckets[i]

	current_highest_number = buckets[current_highest]
	buckets[current_highest] = 0#Reset highest bucket

	for j in range(0, current_highest_number): #Re-distribute
		current_add_index = (current_highest + j + 1) % len(buckets)
		buckets[current_add_index] += 1