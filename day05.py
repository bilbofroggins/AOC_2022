from collections import defaultdict

stacks = defaultdict(list)
unreversed = True
beginning = True
PART_1 = False
PART_2 = True

with open('day05_input.txt') as f:
    for line in f:
        if beginning or line[0] == '[':
            beginning = False
            items = (line[i:i+4] for i in range(0, len(line), 4))
            for i, item in enumerate(items):
                item_val = item[1]
                if item_val == ' ':
                    continue
                stacks[i+1].append(item_val)
        elif line[0] == 'm':
            if unreversed:
                unreversed = False
                for stack in stacks.values():
                    stack.reverse()


            commands = line.strip().split(' ')
            num = int(commands[1])
            from_stack = int(commands[3])
            to_stack = int(commands[5])

            if PART_1:
                for i in range(num):
                    val = stacks[from_stack].pop()
                    stacks[to_stack].append(val)

            elif PART_2:
                temp_stack = []
                for i in range(num):
                    temp_stack.append(stacks[from_stack].pop())
                while temp_stack:
                    stacks[to_stack].append(temp_stack.pop())

res = []
stack_list = list(stacks.items())
stack_list.sort()
for key, stack in stack_list:
    res.append(stack[-1])

print(''.join(res))