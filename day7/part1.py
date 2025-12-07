import unittest
from pathlib import Path


def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    data = []
    with open(base_dir / file_name) as file:
        for line in file:
            if line.rstrip() == '':
                continue
            data.append(list(line.rstrip()))
            

    # print(data)

    splits = 0
    for y in range(0, len(data)-1):
        for x in range(0, len(data[0])):
            if not (data[y][x] in ['S','|']):
                continue

            if data[y+1][x] == '.':
                data[y+1][x] = '|'
            elif data[y+1][x] == '^':
                data[y+1][x-1] = '|'
                data[y+1][x+1] = '|'
                splits += 1
    
    return splits


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 21)

    def test_real_data(self):
        self.assertEqual(main(False), 1602)


unittest.main()
