import unittest
from pathlib import Path

def main(isTest):
    fileName = 'test-data.txt' if isTest else 'data.txt'
    base_dir = Path(__file__).resolve().parent
    data = []
    with open(base_dir / fileName) as file:
        for line in file:
            if line.strip() == '':
                continue
            for interval in line.split(','):
                [start, end] = interval.split('-')
                for n in range(int(start), int(end)+1):
                    data.append(n)
            
            
    invalidIds = []

    def checkId(id, l):
        id_str = str(id)
        half_i = len(id_str) // 2 
        if half_i * 2 == len(id_str) and id_str[0:half_i] == id_str[half_i:]:
            invalidIds.append(id)
        else:
            return

    for id in data:
        checkId(id, 1)
    
    return(sum(invalidIds))

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 1227775554)

    def test_real_data(self):
        self.assertEqual(main(False), 40055209690)

unittest.main()