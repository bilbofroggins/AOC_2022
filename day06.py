from collections import defaultdict

if PART_1:
    NUM_CHARS = 4
else:
    NUM_CHARS = 14

d = defaultdict(int)
with open('day06_input.txt') as f:
    for line in f:
        for i, char in enumerate(line.strip()):
            d[char] += 1

            if i >= NUM_CHARS:
                d[line[i - NUM_CHARS]] -= 1
                if d[line[i - NUM_CHARS]] == 0:
                    d.pop(line[i - NUM_CHARS])
            
            if len(d) == NUM_CHARS:
                print(i + 1)
                exit(0)
