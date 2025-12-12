import unittest
from pathlib import Path

def main(isTest):
    file_name = "test-data.txt" if isTest else "data2.txt"
    base_dir = Path(__file__).resolve().parent
    data = []
    with open(base_dir / file_name) as file:
        for line in file:
            [_dimensons, _presents] = line.rstrip().split(": ")
            dimensions = list(map(int, _dimensons.split('x')))
            presents = list(map(int,_presents.split(' ')))
            data.append([dimensions, presents])
    
    def can_fit_presents(line):
        [dimensions, presents] = line
        [x,y] = dimensions
        area = x*y
        number_of_presents = sum(presents)
        area_of_presents = number_of_presents * 9
        return area_of_presents <= area
    
    return len(list(filter(can_fit_presents, data)))


class Test(unittest.TestCase):
    def test_real_data(self):
        self.assertEqual(main(False), 555)


unittest.main()
