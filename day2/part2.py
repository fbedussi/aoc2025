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
        i = 0
        while i < (len(id_str) - l - l) and id_str[i:i+l] == id_str[i+l:i+l+l]:
            i += l
        if i == (len(id_str) - l - l) and id_str[i:i+l] == id_str[i+l:i+l+l]:
            invalidIds.append(id)
        elif l < len(id_str) // 2:
            return checkId(id, l+1)
        else:
            return

    for id in data:
        checkId(id, 1)
    
    return(sum(list(dict.fromkeys(invalidIds))))

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 4174379265)

    def test_real_data(self):
        self.assertEqual(main(False), 50857215650)

unittest.main()