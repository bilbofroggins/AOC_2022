from collections import deque
grid = []
start_pos = ()
PART_1 = False

with open('day12_input.txt') as f:
    for row, line in enumerate(f):
        grid.append([])
        for col, char in enumerate(line.strip()):
            int_val = ord(char)
            if char == 'S':
                int_val = ord('a') - 1
            elif char == 'E':
                int_val = ord('z')
                start_pos = (row, col)
            grid[-1].append(int_val)

num_rows = len(grid)
num_cols = len(grid[0])

def valid_neighbors(row, col):
    ns = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for n in ns:
        new_row = row + n[0]
        new_col = col + n[1]
        if new_row >= 0 and new_row < num_rows and new_col >= 0 and new_col < num_cols:
            yield (new_row, new_col)

def solve():
    q = deque()
    q.append((start_pos[0], start_pos[1], 0))
    seen = set()
    seen.add((start_pos[0], start_pos[1]))

    while q:
        row, col, num_steps = q.popleft()

        if PART_1 and grid[row][col] == ord('a') - 1:
            return num_steps
        elif (grid[row][col] == ord('a') - 1 or grid[row][col] == ord('a')):
            return num_steps

        for new_row, new_col in valid_neighbors(row, col):
            if (new_row, new_col) not in seen and grid[new_row][new_col] >= grid[row][col] - 1:
                q.append((new_row, new_col, num_steps + 1))
                seen.add((new_row, new_col))

print(solve())
