during_cycles = [1]
x_val = 1

with open('day10_input.txt') as f:
    for line in f:
        line = line.strip()
        if line == 'noop':
            during_cycles.append(x_val)
        else:
            to_add = int(line.split(' ')[1])
            during_cycles.append(x_val)
            during_cycles.append(x_val)
            x_val += to_add


# PART 1
# during the 20th cycle and every 40 cycles after that
indexes = [i for i in range(20, len(during_cycles), 40)]
total = [i * during_cycles[i] for i in indexes]
print(sum(total))

# PART 2
mid_pixel = 2
start_indexes = [i for i in range(0, len(during_cycles) - 1, 40)]
for row in start_indexes:
    line = []
    for col in range(1, 41):
        i = row + col
        mid_pixel = during_cycles[i] + 1
        if abs(col - mid_pixel) < 2:
            line.append('#')
        else:
            line.append('.')
    print(''.join(line))