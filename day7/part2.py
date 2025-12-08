import unittest
from pathlib import Path


def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / file_name) as file:
        data = [list(line.rstrip()) for line in file][::2]

    def get_val(cell):
        match cell:
            case "." | "^":
                return 0
            case "S":
                return 1
            case _:
                return cell

    def is_number(value):
        return isinstance(value, int)

    for y in range(1, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x] == "^":
                continue

            val = get_val(data[y - 1][x])

            if x > 0 and data[y][x - 1] == "^":
                val += get_val(data[y - 1][x - 1])

            if x < len(data[y]) - 1 and data[y][x + 1] == "^":
                val += get_val(data[y - 1][x + 1])

            data[y][x] = val

    return sum(filter(is_number, data[-1]))


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 40)

    def test_real_data(self):
        self.assertEqual(main(False), 135656430050438)


unittest.main()
