with open("day_6_input.in") as file:
    arg_lines = file.read().splitlines()
    last_line = arg_lines[len(arg_lines) - 1]
    problem_indexes = []
    for symbol_idx in range(0, len(last_line)):
        if last_line[symbol_idx] == " ":
            continue
        problem_indexes.append((symbol_idx, last_line[symbol_idx]))
    
    total_sum = 0
    for problem_idx in range(0, len(problem_indexes)):
        is_sum = problem_indexes[problem_idx][1] == "+"
        problem_result = 0 if is_sum else 1
        for line_numbers in arg_lines[:len(arg_lines) - 1]:
            right_bound = problem_indexes[problem_idx + 1][0] if problem_idx + 1 < len(problem_indexes) else len(line_numbers)
            number = line_numbers[problem_indexes[problem_idx][0]:right_bound]
            if is_sum:
                problem_result += int(number)
            else:
                problem_result *= int(number)
        total_sum += problem_result
    print(total_sum)