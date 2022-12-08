grid = []
row = 0
with open('day08_input.txt') as f:
    for line in f:
        grid.append([])
        for char in line.strip():
            grid[row].append(int(char))

        row += 1

num_rows = len(grid)
num_cols = len(grid[0])

def part1():
    visible = set()
    for row in range(num_rows):
        max_val = -1
        for col in range(num_cols):
            if grid[row][col] > max_val:
                visible.add((row, col))
                max_val = grid[row][col]
    for row in range(num_rows):
        max_val = -1
        for col in range(num_cols - 1, -1, -1):
            if grid[row][col] > max_val:
                visible.add((row, col))
                max_val = grid[row][col]
    for col in range(num_cols):
        max_val = -1
        for row in range(num_rows):
            if grid[row][col] > max_val:
                visible.add((row, col))
                max_val = grid[row][col]
    for col in range(num_cols):
        max_val = -1
        for row in range(num_rows - 1, -1, -1):
            if grid[row][col] > max_val:
                visible.add((row, col))
                max_val = grid[row][col]

    print(len(visible))

def num_trees(position, direction):
    orig_position = position
    i = 0
    while (position[0] + direction[0] > -1 and position[0] + direction[0] < num_rows
    and position[1] + direction[1] > -1 and position[1] + direction[1] < num_cols):
        position = tuple(map(sum, zip(position, direction)))
        i += 1
        if grid[position[0]][position[1]] >= grid[orig_position[0]][orig_position[1]]:
            break

    return i

def part2():
    max_score = 0
    for row in range(1, num_rows - 1):
        for col in range(1, num_cols - 1):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #u, d, l, r
            trees = 1
            for direction in directions:
                trees *= num_trees((row, col),direction)
            
            max_score = max(max_score, trees)

    print(max_score)

part1()
part2()
