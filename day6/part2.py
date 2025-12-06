import unittest
from pathlib import Path


def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    data = []
    with open(base_dir / file_name) as file:
        for line in file:
            data.append(list(line.replace("\n", "")))

    def rotate(matrix):
        result = []
        for _ in range(len(matrix[0])):
            result.append([""] * len(matrix))
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[y])):
                result[-1 -x][y] = matrix[y][x]

        return result

    rotated = rotate(data)

    operations = [[]]
    for line in rotated:
        if "".join(line).strip() == "":
            operations.append([])
            continue

        n = "".join(line[:-1]).strip()
        operations[-1].append(int(n))
        last_char = line[-1]
        if last_char in ['+', '*']:
            operations[-1].append(last_char)

    results = []
    for operation in operations:
        result = operation[0]
        for n in operation[1:-1]:
            if operation[-1] == "+":
                result += n
            else:
                result *= n

        results.append(result)

    return sum(results)


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 3263827)

    def test_real_data(self):
        self.assertEqual(main(False), 10442199710797)


unittest.main()
