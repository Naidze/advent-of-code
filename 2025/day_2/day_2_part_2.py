def fill_divisors_set(num_str):
    divisors_set = set()
    for num in range(1, len(num_str)):
        if len(num_str) % num == 0:
            divisors_set.add(int(num))
    return divisors_set


def check_all_divisors(num_str, divisors_set):
    for divisor in divisors_set:
        candidate_block = num_str[:divisor]
    repetition_count = (len(num_str)//divisor)
        if num_str == candidate_block * repetition_count:
            return True
    return False


def process_number_range(start, stop):
    invalid_ids = []
    for number in range(start, stop + 1):
        num_str = str(number)
        divisors_set = fill_divisors_set(num_str)
        if check_all_divisors(num_str, divisors_set):
            invalid_ids.append(num_str)
    return invalid_ids


with open("day_2_input.in") as file:
    invalid_ids = []
    ranges = file.read().split(",")
    for num_range in ranges:
        start, stop = num_range.split("-")
        invalid_ids.extend(process_number_range(int(start), int(stop)))

    total = sum([int(num) for num in invalid_ids])
    print(total)
