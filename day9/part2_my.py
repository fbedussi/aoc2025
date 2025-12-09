import unittest
from pathlib import Path

# This is an implementation of an algorithm I designed:

# Is the point inside the polygon?
# If the point is on a border segment → YES, it's inside

# Otherwise, count all vertices that are in the 4 quadrants that divide the plane starting from the point:

# Top-left quadrant: x < point.x AND y < point.y
# Top-right quadrant: x > point.x AND y < point.y
# Bottom-right quadrant: x > point.x AND y > point.y
# Bottom-left quadrant: x < point.x AND y > point.y
# The point is inside if:

# All 4 quadrants have at least one vertex (count > 0)
# All 4 quadrants have an odd number of vertices

# but unfortunately it works only with the test data, not with the real one


def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / file_name) as file:
        data = list(list(map(int, line.rstrip().split(","))) for line in file)
        
    max_area = None

    def is_included(a, b, c):
        return (a >= b and b >= c) or (c <= b and b <= c)

    def is_in_segment(x, y, point1, point2):
        if point1[0] == x and point2[0] == x and is_included(point1[1], y, point2[1]):
            return True

        if point1[1] == y and point2[1] == y and is_included(point1[0], x, point2[0]):
            return True

        return False

    def is_on_border(x, y):
        for i in range(0, len(data)-1):
            if is_in_segment(x, y, data[i], data[i + 1]):
                return True

        # check also the last+first pair
        return is_in_segment(x, y, data[-1], data[0])

    def is_inside(x, y):
        if is_on_border(x, y):
            return True

        top_left = 0
        top_right = 0
        bottom_right = 0
        bottom_left = 0
        for point in data:
            if point[0] < x and point[1] < y:
                top_left += 1
            elif point[0] > x and point[1] < y:
                top_right += 1
            elif point[0] > x and point[1] > y:
                bottom_right += 1
            if point[0] < x and point[1] > y:
                bottom_left += 1

        return (
            top_left != 0
            and top_right != 0
            and bottom_right != 0
            and bottom_left != 0
            and (top_left % 2 != 0)
            and (top_right % 2 != 0)
            and (bottom_right % 2 != 0)
            and (bottom_left % 2 != 0)
        )

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
        self.assertEqual(main(False), 4781377701)


unittest.main()
# 4602484064 high
