with open("day_2_input.in") as file:
    invalid_ids = []
    ranges = file.read().split(",")
    for num_range in ranges:
        start, stop = num_range.split("-")
        for number in range(int(start), int(stop) + 1):
            num_str = str(number)
            num_length = len(num_str)
            if num_length % 2 != 0:
                continue

            mid_part = num_length // 2
            idx = 0
            valid = True
            while idx < mid_part:
                if num_str[idx] != num_str[mid_part + idx]:
                    valid = False
                    break
                idx += 1

            if valid:
                invalid_ids.append(num_str)
    total = sum([int(num) for num in invalid_ids])
    print(total)
