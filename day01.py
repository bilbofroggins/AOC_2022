def part1():
    calories = [0]

    with open('day01_input.txt') as f:
        elf = 0
        for line in f:
            val = line.strip()
            if val == "":
                elf += 1
                calories.append(0)
                continue

            calories[elf] += int(val)

    calories.sort(reverse=True)
    print(calories[0])

def part2():
    calories = [0]

    with open('day01_input.txt') as f:
        elf = 0
        for line in f:
            val = line.strip()
            if val == "":
                elf += 1
                calories.append(0)
                continue

            calories[elf] += int(val)

    calories.sort(reverse=True)
    print(calories[0] + calories[1] + calories[2])

part1()
part2()
