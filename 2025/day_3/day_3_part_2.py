BATTERIES_LENGTH = 12

def find_max(num_list):
    max_idx = 0
    max = int(num_list[max_idx])
    for i in range(1, len(num_list)):
        if int(num_list[i]) > max:
            max = int(num_list[i])
            max_idx = i
    return max_idx, max

def get_block_max(block):
    start_idx = 0
    max_sum = 0
    for batteries_left in range(BATTERIES_LENGTH, 0, -1):
        max_idx, max = find_max(block[start_idx:len(block) - batteries_left + 1])
        max_sum += pow(10, batteries_left - 1) * max
        start_idx = start_idx + max_idx + 1
    return max_sum

with open("day_3_input.in") as file:
    blocks = file.read().split("\n")
    joltage_sum = 0
    for block in blocks:
        joltage_sum += get_block_max(block)
    print(joltage_sum)