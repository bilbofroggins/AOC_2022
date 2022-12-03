def item_val(char):
    if ord(char) < 97:
        return ord(char) - 38
    return ord(char) - 96

def part1():
    res = 0
    with open('day03_input.txt') as f:
        for line in f:
            line = line.strip()
            half_length = int(len(line) / 2)
            start_items = line[:half_length]
            end_items = line[half_length:]

            start_set = set()
            for item in start_items:
                start_set.add(item)

            for item in end_items:
                if item in start_set:
                    res += item_val(item)
                    break

    print(res)

def part2():
    res = 0
    with open('day03_input.txt') as f:
        s = set()
        i = 0
        for line in f:
            temp_set = set()
            line = line.strip()

            for item in line:
                if i == 0:
                    temp_set.add(item)
                elif item in s:
                    temp_set.add(item)

            s = temp_set
            if i == 2:
                res += item_val(list(s)[0])
                i = 0
            else:
                i += 1

    print(res)

part1()
part2()