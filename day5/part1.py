import unittest
from pathlib import Path

def main(isTest):
    file_name = 'test-data.txt' if isTest else 'data.txt'
    base_dir = Path(__file__).resolve().parent
    ranges = []
    ids = []
    with open(base_dir / file_name) as file:
        ranges_ended = False
        for line in file:
            if line.rstrip() == '':
                ranges_ended = True
                continue
            if not ranges_ended:
                [start, end] = line.rstrip().split('-') 
                ranges.append([int(start), int(end)])
            else:
                ids.append(int(line.rstrip()))
            

    def is_fresh(id):
        result = False

        for [min, max] in ranges:
            if id >= min and id <= max:
                result = True
                break

        return result
            
    fresh_ids = []

    for id in ids:
        if is_fresh(id):
            fresh_ids.append(id)
            
    
    return(len(fresh_ids))

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 3)

    def test_real_data(self):
        self.assertEqual(main(False), 598)

unittest.main()