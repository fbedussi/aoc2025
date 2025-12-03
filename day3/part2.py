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
            bank = []
            for n in line:
                if n != '\n':
                    bank.append(int(n))
            data.append(bank)
            
            
    maxJoltage = []

    def getMaxJoltage(bank):
        digits = []
        for digits_left in range(11,-1, -1):
            m = max(bank[:-digits_left] if digits_left > 0 else bank) 
            digits.append(m)
            bank = bank[bank.index(m)+1:]
            
        return int(''.join(str(n) for n in digits))
    

    for bank in data:
        maxJoltage.append(getMaxJoltage(bank))
    
    return(sum(maxJoltage))

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 3121910778619)

    def test_real_data(self):
        self.assertEqual(main(False), 176582889354075)

unittest.main()