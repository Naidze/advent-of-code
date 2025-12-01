f = open('day_1_input.in', 'r', encoding="utf-8")
turns = f.read().split("\n")
curr_idx = 50
zero_count = 0
times_around = 0

for turn in turns:
	direction = -1 if turn[0] == "L" else 1
	distance  = int(turn[1:])
	
	if direction == 1:
		needed = (100 - curr_idx) % 100
	else:
		needed = curr_idx % 100

	if needed == 0:
		needed = 100

	if distance >= needed:
		hits = 1 + (distance - needed) // 100
		zero_count += hits

	curr_idx = (curr_idx + direction * distance) % 100
		
print(zero_count + times_around)