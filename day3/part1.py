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

    def findMax(bank):
        m = max(bank)
        m_index = bank.index(m)
        if m_index > len(bank) - 2:
            return findMax(bank[:m_index] + [0] + bank[m_index+1:])
        else:
            return m

    def getMaxJoltage(bank):
        first = findMax(bank)
        first_index = bank.index(first)
        second = max(bank[first_index+1:])
        return int(str(first) + str(second))
    

    for bank in data:
        maxJoltage.append(getMaxJoltage(bank))
    
    return(sum(maxJoltage))

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 357)

    def test_real_data(self):
        self.assertEqual(main(False), 17766)

unittest.main()