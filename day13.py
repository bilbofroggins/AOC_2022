import ast, math

comparisons = []

with open('day13_input.txt') as f:
    for row, line in enumerate(f):
        if row % 3 == 0:
            comparisons.append([None, None])
            comparisons[-1][0] = ast.literal_eval(line.strip())
        elif row %3 == 1:
            comparisons[-1][1] = ast.literal_eval(line.strip())

def compare(item1, item2):
    if isinstance(item1, list) and isinstance(item2, list):
        i = 0
        while i < len(item2):
            if i >= len(item1):
                return True
            res = compare(item1[i], item2[i])
            if res != None:
                return res
            i += 1
    elif isinstance(item1, int) and isinstance(item2, int):
        if item1 == item2:
            return None
        elif item1 < item2:
            return True
        else:
            return False
    elif isinstance(item1, list):
        return compare(item1, [item2])
    else:
        return compare([item1], item2)

    if len(item1) > len(item2):
        return False

# PART 1
total = 0
i = 1
for comparison in comparisons:
    if compare(comparison[0], comparison[1]):
        total += i
    i += 1
print(total)

# PART 2
sorted_comparisons = []
comparisons = [item for sublist in comparisons for item in sublist]
for comparison in comparisons:
    insert_pos = None
    for i in range(len(sorted_comparisons)):
        if compare(comparison, sorted_comparisons[i]):
            insert_pos = i
            sorted_comparisons.insert(i, comparison)
            break
    if insert_pos == None:
        sorted_comparisons.append(comparison)

insert_positions = []
dividers = [[[2]], [[6]]]
for divider in dividers:
    insert_pos = None
    for i in range(len(sorted_comparisons)):
        if compare(divider, sorted_comparisons[i]):
            insert_pos = i
            sorted_comparisons.insert(i, divider)
            break
    if insert_pos == None:
        insert_pos = len(sorted_comparisons)
        sorted_comparisons.append(divider)

    insert_positions.append(insert_pos + 1)

print(math.prod(insert_positions))

