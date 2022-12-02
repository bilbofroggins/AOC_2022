def win_pts(my_move, elf_move):
    vals = {'A':0, 'B':1, 'C':2}
    diff = (vals[my_move] % 3) - (vals[elf_move] % 3)
    if diff == 1:
        return 6
    elif diff == 0:
        return 3
    return 0

def part1():
    points = {'A':1, 'B':2, 'C':3}
    x_to_az = {'X':'A', 'Y':'B', 'Z':'C'}

    total_points = 0

    with open('day2_input.txt') as f:
        for line in f:
            elf_move, my_move = line.strip().split(' ')

            shape_points = points[x_to_az[my_move]]
            win_points = win_pts(x_to_az[my_move], elf_move)
            total_points += (shape_points + win_points)

        print(total_points)


part1()