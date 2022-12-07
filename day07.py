class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.filesize_total = 0
        self.children_dirs = {}
        self.parent = parent

tree = Node('/')
node = tree

filehandle = open('day07_input.txt', 'r')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    line = line.strip()
    # print("New section")

    if line == '$ cd /':
        continue
    elif line == '$ ls':
        fz = node.filesize_total
        childz = len(node.children_dirs) > 0
        while True:
            line = filehandle.readline()
            if not line:
                break
            line = line.strip()

            if line[0] == '$':
                break
            elif fz or childz:
                continue
            elif line[:3] == 'dir':
                node.children_dirs[line[4:]] = Node(line[4:], node)
            else:
                node.filesize_total += int(line.split(' ')[0])

            # print(line, node.filesize_total)

    if line == '$ cd ..':
        node = node.parent
    elif line[:5] == '$ cd ':
        node = node.children_dirs[line[5:]]

dirs_over_10000 = []
all_dir_sizes = []
def parse_tree(node):
    dir_size = 0
    for child in node.children_dirs.values():
        dir_size += parse_tree(child)

    total_size = node.filesize_total + dir_size
    # PART 1
    if total_size <= 100000:
        dirs_over_10000.append(total_size)
    # PART 2
    all_dir_sizes.append(total_size)
    return total_size

parse_tree(tree)

print(sum(dirs_over_10000))

all_dir_sizes.sort()
for dir_size in all_dir_sizes:
    if 70000000 - all_dir_sizes[-1] + dir_size >= 30000000:
        print(dir_size)
        break

filehandle.close()