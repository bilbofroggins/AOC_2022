def win_pts(my_move, elf_move):
    vals = {'A':0, 'B':1, 'C':2}
    diff = vals[my_move] - vals[elf_move]
    if diff == 1 or diff == -2:
        return 6
    elif diff == 0:
        return 3
    return 0

def move(result, elf_move):
    res = ['A', 'B', 'C']
    vals = {'A':0, 'B':1, 'C':2}
    result_inc = {'X':-1, 'Y':0, 'Z':1}
    return res[(vals[elf_move] + result_inc[result]) % 3]

def part1():
    points = {'A':1, 'B':2, 'C':3}
    x_to_az = {'X':'A', 'Y':'B', 'Z':'C'}

    total_points = 0

    with open('day02_input.txt') as f:
        for line in f:
            elf_move, my_move = line.strip().split(' ')

            shape_points = points[x_to_az[my_move]]
            win_points = win_pts(x_to_az[my_move], elf_move)
            total_points += (shape_points + win_points)

        print(total_points)

def part2():
    points = {'A':1, 'B':2, 'C':3}
    win_pts = {'X':0, 'Y':3, 'Z':6}

    total_points = 0

    with open('day02_input.txt') as f:
        for line in f:
            elf_move, my_result = line.strip().split(' ')

            shape_points = points[move(my_result, elf_move)]
            win_points = win_pts[my_result]
            total_points += (shape_points + win_points)

        print(total_points)


part1()
part2()
