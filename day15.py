from collections import defaultdict

target_row = 2000000

target_row_hashes = set()
beacon_data = defaultdict(list)
sensor_data = defaultdict(list)
with open('day15_input.txt') as f:
    for line in f:
        s, b = line.strip().split(':')
        sx_un, sy_un = s.split(',')
        bx_un, by_un = b.split(',')

        sensor_col = int(sx_un.split('=')[1])
        sensor_row = int(sy_un.split('=')[1])
        beacon_col = int(bx_un.split('=')[1])
        beacon_row = int(by_un.split('=')[1])
        beacon_data[beacon_row].append(beacon_col)
        sensor_data[sensor_row].append(sensor_col)

        dist_to_beacon = abs(beacon_col - sensor_col) + abs(beacon_row - sensor_row)
        diff = dist_to_beacon - abs(target_row - sensor_row)
        if diff > dist_to_beacon:
            continue

        for i in range(diff + 1):
            target_row_hashes.add(sensor_col + i)
            target_row_hashes.add(sensor_col - i)

print(len(target_row_hashes - set(beacon_data[target_row]) - set(sensor_data[target_row])))

