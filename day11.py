from collections import deque
from math import lcm

PART_1 = False
num_rounds = 20 if PART_1 else 10000

class Monkey:
    def __init__(self, items, inspection_eq, throw_eq):
        self.items = deque(items)
        self.inspection_eq = inspection_eq
        self.throw_eq = throw_eq
        self.inspect_count = 0

    def inspect(self):
        self.inspect_count += 1
        item = self.items.popleft()
        item = self.inspection_eq(item)
        if PART_1:
            item = item // 3

        throw_to = self.throw_eq(item)
        monkeys[throw_to].items.append(item % multiple)

    def __repr__(self):
        return ','.join([str(i) for i in self.items])


monkey0 = Monkey(
    [72, 64, 51, 57, 93, 97, 68],
    lambda x: x*19,
    lambda x: 4 if x%17 == 0 else 7
)
monkey1 = Monkey(
    [62],
    lambda x: x*11,
    lambda x: 3 if x%3 == 0 else 2
)
monkey2 = Monkey(
    [57, 94, 69, 79, 72],
    lambda x: x+6,
    lambda x: 0 if x%19 == 0 else 4
)
monkey3 = Monkey(
    [80, 64, 92, 93, 64, 56],
    lambda x: x+5,
    lambda x: 2 if x%7 == 0 else 0
)
monkey4 = Monkey(
    [70, 88, 95, 99, 78, 72, 65, 94],
    lambda x: x+7,
    lambda x: 7 if x%2 == 0 else 5
)
monkey5 = Monkey(
    [57, 95, 81, 61],
    lambda x: x*x,
    lambda x: 1 if x%5 == 0 else 6
)
monkey6 = Monkey(
    [79, 99],
    lambda x: x+2,
    lambda x: 3 if x%11 == 0 else 1
)
monkey7 = Monkey(
    [68, 98, 62],
    lambda x: x+3,
    lambda x: 5 if x%13 == 0 else 6
)

multiple = lcm(17, 3, 19, 7, 2, 5, 11, 13)

monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

for i in range(num_rounds):
    for monkey in monkeys:
        for item in range(len(monkey.items)):
            monkey.inspect()

sorted_inspect_counts = []
for monkey in monkeys:
    sorted_inspect_counts.append(monkey.inspect_count)
sorted_inspect_counts.sort(reverse=True)
print(sorted_inspect_counts[0]*sorted_inspect_counts[1])