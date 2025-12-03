def find_max(num_list):
    max_idx = 0
    max = int(num_list[max_idx])
    for i in range(1, len(num_list)):
        if int(num_list[i]) > max:
            max = int(num_list[i])
            max_idx = i
    return max_idx, max

def get_block_max(block):
    num_list_l = block[:len(block) - 1]
    max_idx_l, max_l = find_max(num_list_l)

    num_list_r = [int(num) for num in block[max_idx_l + 1:len(block)]]
    _, max_r = find_max(num_list_r)

    return 10 * max_l + max_r

with open("day_3_input.in") as file:
    blocks = file.read().split("\n")
    joltage_sum = 0
    for block in blocks:
        joltage_sum += get_block_max(block)
    print(joltage_sum)