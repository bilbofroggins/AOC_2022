res = 0
with open('day04_input.txt') as f:
    for line in f:
        first_range, second_range = line.strip().split(',')
        first_range = first_range.split('-')
        second_range = second_range.split('-')
        first_range = list(map(int, first_range))
        second_range = list(map(int, second_range))

        #part1
        if (first_range[0] <= second_range[0] and
            first_range[1] >= second_range[1]) or (second_range[0] <= first_range[0] and
            second_range[1] >= first_range[1]):
            res += 1
        #part2
        elif (second_range[0] <= first_range[1] and
            second_range[0] >= first_range[0]) or (second_range[1] <= first_range[1] and
            second_range[1] >= first_range[0]):
            res += 1

print(res)