import unittest
from pathlib import Path
import math


def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / file_name) as file:
        data = list(
            map(
                lambda x: [x, None],
                [list(map(int, line.rstrip().split(","))) for line in file],
            )
        )

    next_group_index = 0

    def calculate_distance(a, b):
        [xa, ya, za] = a
        [xb, yb, zb] = b
        return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2 + (za - zb) ** 2)

    distances = {}

    def calculate_distances():
        for y1 in range(0, len(data)):
            for y2 in range(0, len(data)):
                if y1 == y2:
                    continue

                key = "_".join(sorted([str(y1), str(y2)]))

                if key in distances:
                    continue

                line1 = data[y1]
                line2 = data[y2]

                distances[key] = calculate_distance(line1[0], line2[0])

    def group(i1, i2):
        nonlocal next_group_index
        if data[i1][1] == None and data[i2][1] == None:
            data[i1][1] = next_group_index
            data[i2][1] = next_group_index
            next_group_index += 1
        elif data[i1][1] != None and data[i2][1] == None:
            data[i2][1] = data[i1][1]
        elif data[i2][1] != None and data[i1][1] == None:
            data[i1][1] = data[i2][1]
        elif data[i1][1] != None and data[i2][1] != None:
            index_to_change = data[i2][1]
            for line in data:
                if line[1] == index_to_change:
                    line[1] = data[i1][1]

    calculate_distances()

    distances_sorted = list(distances.items())
    distances_sorted.sort(key=lambda x: x[1])

    for i in range(0, 10 if isTest else 1000):
        [longest_circuits, b] = list(map(int, distances_sorted[i][0].split("_")))
        group(longest_circuits, b)

    circuits = {}
    for line in data:
        if line[1] == None:
            continue
        elif line[1] in circuits:
            circuits[line[1]] += 1
        else:
            circuits[line[1]] = 1

    longest_circuits = list(circuits.values())
    longest_circuits.sort(reverse=True)

    return longest_circuits[0] * longest_circuits[1] * longest_circuits[2]


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 40)

    def test_real_data(self):
        self.assertEqual(main(False), 352584)


unittest.main()
