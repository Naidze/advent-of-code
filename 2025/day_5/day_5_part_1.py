with open("day_5_input.in") as file:
    ingridients_data = file.read().splitlines()
    fresh_ranges = []
    empty_line_idx = 0
    for line in ingridients_data:
        if not line.strip():
            break
        fresh_ranges.append(line)
        empty_line_idx += 1

    available_ingredients = ingridients_data[empty_line_idx  + 1::]

    fresh_count = 0
    accounted_ingredients = set()
    for ingredient in available_ingredients:
        for fresh_range in fresh_ranges:
            start, end = fresh_range.split("-")
            if int(ingredient) >= int(start) and int(ingredient) <= int(end) and int(ingredient) not in accounted_ingredients:
                fresh_count += 1
                accounted_ingredients.add(int(ingredient))
    print(fresh_count)
