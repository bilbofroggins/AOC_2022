segments = []
points = []
all_cols = []
all_rows = []
PART_2 = True
with open('day14_input.txt') as f:
    for line in f:
        points = line.strip().split(' -> ')
        cs = [int(point.split(',')[0]) for point in points]
        for c in cs:
            all_cols.append(c)
        rs = [int(point.split(',')[1]) for point in points]
        for r in rs:
            all_rows.append(r)
        segments.append(points)

min_col = min(all_cols) - 1
max_col = max(all_cols) + 1
if PART_2:
    min_col = min_col - (max_col - min_col)*10
    max_col = max_col + (max_col - min_col)*10
min_row = 0
max_row = max(all_rows) + 2
grid = [['.']*(max_col - min_col + 1) for i in range(max_row + 1)]

def norm_col(col):
    return col - min_col

for points in segments:
    last_col, last_row = None, None
    for point in points:
        col, row = point.split(',')
        col = int(col)
        row = int(row)
        if last_col != None:
            diff_col = col - last_col
            diff_row = row - last_row
            if diff_col == 0:
                dir = int(diff_row // abs(diff_row))
                for r in range(last_row, last_row + diff_row + dir, dir):
                    grid[r][norm_col(col)] = '#'
            else:
                dir = int(diff_col // abs(diff_col))
                for c in range(last_col, last_col + diff_col + dir, dir):
                    grid[row][norm_col(c)] = '#'

        last_col, last_row = col, row

if PART_2:
    for col, _ in enumerate(grid[-1]):
        grid[-1][col] = '#'

def do_sand():
    count = 0
    while True:
        count += 1
        sand = [0, norm_col(500)]

        while True:
            if sand[0] == max_row and not PART_2:
                return count - 1
            if grid[sand[0] + 1][sand[1]] == '.':
                sand[0] += 1
                continue
            if grid[sand[0] + 1][sand[1] - 1] == '.':
                sand[0] += 1
                sand[1] -= 1
                continue
            if grid[sand[0] + 1][sand[1] + 1] == '.':
                sand[0] += 1
                sand[1] += 1
                continue
            grid[sand[0]][sand[1]] = '#'
            if PART_2 and sand[0] == 0:
                return count
            break

print(do_sand())