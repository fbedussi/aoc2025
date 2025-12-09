import unittest
from pathlib import Path


# This is the implementation of the first algorithm suggested here:
# https://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
# that seems reasonable to me, and is simple to implement in a case like this where all the side to intersect are just vertical
# but unfortunately it works only with the test data, not with the real one

    
def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / file_name) as file:
        data = list(list(map(int, line.rstrip().split(","))) for line in file)

    max_area = None

    def is_included(a, b, c):
        return (a >= b and b >= c) or (a <= b and b <= c)

    def is_inside(x, y):
        intersections = 0
        for i in range(0, len(data)):
            # consider also the last+first pair
            next_i = (i + 1) % len(data)

            if data[i][1] == data[next_i][1]:
                # consider only vertical segments, aka with different y
                continue

            if x > data[i][0]:
                # the point is external on the right
                continue

            if is_included(data[i][1], y, data[next_i][1]):
                intersections += 1

        return (intersections != 0) and (intersections % 2 != 0)

    for point1 in data:
        for point2 in data:
            if point1 == point2 or point1[0] == point2[0] or point1[1] == point2[1]:
                continue

            if not is_inside(point1[0], point2[1]):
                continue

            if not is_inside(point2[0], point1[1]):
                continue

            area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
            if (max_area == None) or (area > max_area):
                max_area = area

    return max_area


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 24)

    def test_real_data(self):
        self.assertEqual(main(False), None)


unittest.main()
# 4602484064 high
# 4764108305 hight
