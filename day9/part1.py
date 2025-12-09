import unittest
from pathlib import Path
import math


def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / file_name) as file:
        data = list(list(map(int, line.rstrip().split(","))) for line in file)

    max_area = None

    for point1 in data:
        for point2 in data:
            if point1 == point2 or point1[0] == point2[0] or point1[1] == point2[1]:
                continue

            area = (abs(point1[0] - point2[0])+1) * (abs(point1[1] - point2[1])+1)
            if (max_area == None) or (area > max_area):
                max_area = area

    return max_area


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 50)

    def test_real_data(self):
        self.assertEqual(main(False), 4781377701)


unittest.main()
