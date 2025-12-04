def check_horizontal(grid_lines, x, y):
    reach_count = 0
    if x == 0 or grid_lines[y][x - 1] == ".":
        reach_count += 1
    if x == len(grid_lines[y]) - 1 or grid_lines[y][x + 1] == ".":
        reach_count += 1
    return reach_count


def check_vertical(grid_lines, x, y):
    reach_count = 0
    if y == 0 or grid_lines[y - 1][x] == ".":
        reach_count += 1
    if y == len(grid_lines) - 1 or grid_lines[y + 1][x] == ".":
        reach_count += 1
    return reach_count


def check_diagonal(grid_lines, x, y):
    reach_count = 0
    # top left
    if x == 0 or y == 0 or grid_lines[y - 1][x - 1] == ".":
        reach_count += 1
    # top right
    if x == len(grid_lines[y]) - 1 or y == 0 or grid_lines[y - 1][x + 1] == ".":
        reach_count += 1
    # bottom left
    if x == 0 or y == len(grid_lines) - 1 or grid_lines[y + 1][x - 1] == ".":
        reach_count += 1
    # bottom right
    if x == len(grid_lines[y]) - 1 or y == len(grid_lines) - 1 or grid_lines[y + 1][x + 1] == ".":
        reach_count += 1
    return reach_count

def update_grid(grid, moved_coordinates):
    for pos in moved_coordinates:
        grid[pos[0]][pos[1]] = "."
    return grid

def count_and_process(grid_lines):
    grid = [list(line) for line in grid_lines]
    total_count = 0
    moved_coordinates = set()
    for line_idx in range(0, len(grid_lines)):
        for obj_idx in range(0, len(grid_lines[line_idx])):
            if (grid[line_idx][obj_idx] == '.'):
                continue

            reach_count = check_horizontal(grid, obj_idx, line_idx) + check_vertical(grid, obj_idx, line_idx) + check_diagonal(grid, obj_idx, line_idx)

            if reach_count > 4:
                total_count += 1
                moved_coordinates.add((line_idx, obj_idx))

    new_grid = update_grid(grid, moved_coordinates)
    return new_grid, total_count


with open("day_4_input.in") as file:
    grid_lines = file.read().splitlines()
    total_count = 0
    while True:
        grid_lines, count = count_and_process(grid_lines)
        if count == 0:
            break
        total_count += count
    print(total_count)
