def check_horizontal(grid_lines, x, y):
    edge_count = 0
    if x == 0 or grid_lines[y][x - 1] == ".":
        edge_count += 1
    if x == len(grid_lines[y]) - 1 or grid_lines[y][x + 1] == ".":
        edge_count += 1
    return edge_count


def check_vertical(grid_lines, x, y):
    edge_count = 0
    if y == 0 or grid_lines[y - 1][x] == ".":
        edge_count += 1
    if y == len(grid_lines) - 1 or grid_lines[y + 1][x] == ".":
        edge_count += 1
    return edge_count


def check_diagonal(grid_lines, x, y):
    edge_count = 0
    # top left
    if x == 0 or y == 0 or grid_lines[y - 1][x - 1] == ".":
        edge_count += 1
    # top right
    if x == len(grid_lines[y]) - 1 or y == 0 or grid_lines[y - 1][x + 1] == ".":
        edge_count += 1
    # bottom left
    if x == 0 or y == len(grid_lines) - 1 or grid_lines[y + 1][x - 1] == ".":
        edge_count += 1
    # bottom right
    if x == len(grid_lines[y]) - 1 or y == len(grid_lines) - 1 or grid_lines[y + 1][x + 1] == ".":
        edge_count += 1
    return edge_count


with open("day_4_input.in") as file:
    grid_lines = file.read().split("\n")
    total_count = 0
    for line_idx in range(0, len(grid_lines)):
        for obj_idx in range(0, len(grid_lines[line_idx])):
            if (grid_lines[line_idx][obj_idx] == '.'):
                continue
            edge_count = 0
            edge_count += check_horizontal(grid_lines, obj_idx, line_idx)
            edge_count += check_vertical(grid_lines, obj_idx, line_idx)
            edge_count += check_diagonal(grid_lines, obj_idx, line_idx)
            if edge_count > 4:
                total_count += 1
    print(total_count)
