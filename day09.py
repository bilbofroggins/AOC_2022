class Vector:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
    def __add__(self, other):
        return Vector(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Vector(self.row - other.row, self.col - other.col)

    def within_one(self, other):
        vec = self - other
        if abs(vec.row) > 1 or abs(vec.col) > 1:
            return False
        return True

    def normalize(self):
        if self.row >= 0:
            self.row = min(1, self.row)
        else:
            self.row = max(-1, self.row)

        if self.col >= 0:
            self.col = min(1, self.col)
        else:
            self.col = max(-1, self.col)
        return self

    def to_tuple(self):
        return (self.row, self.col)

GRID_SIZE = 100
PART_ONE = False
if PART_ONE:
    ROPE_LENGTH = 2
else:
    ROPE_LENGTH = 10

grid = [[0]*GRID_SIZE for i in range(GRID_SIZE)]
rope = [Vector(int(GRID_SIZE/2), int(GRID_SIZE/2))] * ROPE_LENGTH

up = Vector(-1, 0)
down = Vector(1, 0)
left = Vector(0, -1)
right = Vector(0, 1)

tail_positions = set()
tail_positions.add(rope[-1].to_tuple())

def print_grid():
    for row in range(len(grid)):
        line = []
        for col in range(len(grid[0])):
            line.append('.')
            for k, knot in enumerate(rope):
                if knot.row == row and knot.col == col:
                    line[-1] = str(k)
                    break
        print(''.join(line))


with open('day09_input.txt') as f:
    for line in f:
        dir, mag = line.split(' ')
        mag = int(mag)

        if dir == 'U':
            head_move = up
        elif dir == 'D':
            head_move = down
        elif dir == 'L':
            head_move = left
        elif dir == 'R':
            head_move = right

        for _ in range(mag):
            rope[0] = rope[0] + head_move
            for i in range(len(rope) - 1):
                if rope[i].within_one(rope[i + 1]):
                    continue
                diff = rope[i] - rope[i + 1]
                rope[i + 1] += diff.normalize()

            tail_positions.add(rope[-1].to_tuple())

print(len(tail_positions))
