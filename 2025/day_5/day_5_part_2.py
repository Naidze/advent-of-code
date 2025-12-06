def merge_ranges(ranges):
    merged = []
    for start, end in sorted(ranges):
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

ranges = []
with open("day_5_input.in") as file:
    for line in file:
        if not line.strip():
            break
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

merged_ranges = merge_ranges(ranges)
total_unique_ids = sum(end - start + 1 for start, end in merged_ranges)

print(total_unique_ids)
