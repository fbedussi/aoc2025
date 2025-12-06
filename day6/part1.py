import unittest
from pathlib import Path


def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    data = []
    with open(base_dir / file_name) as file:
        for line in file:
            data.append(
                list(
                    map(
                        lambda s: s if s == "+" or s == "*" else int(s),
                        filter(
                            lambda s: len(s) > 0,
                            map(lambda s: s.strip(), line.rstrip().split(" ")),
                        ),
                    )
                )
            )

    results = []
    op_i = len(data) - 1
    for x in range(0, len(data[0])):
        r = data[0][x]
        for y in range(1, len(data) - 1):
            if data[op_i][x] == "+":
                r += data[y][x]
            else:
                r *= data[y][x]
        results.append(r)

    return sum(results)


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 4277556)

    def test_real_data(self):
        self.assertEqual(main(False), 6169101504608)


unittest.main()
