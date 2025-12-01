import unittest

def main(isTest):
    fileName = 'test-data.txt' if isTest else 'data.txt'

    data = []
    with open(fileName, 'r') as file:
        for line in file:
            if line.strip() == '':
                continue
            first_char = line[0]
            rest = line[1:]
            data.append(int(rest) if first_char == 'R' else -int(rest)   )
            
            
    value = 50

    zeroes = 0

    for rotation in data:
        newValue = value + rotation
        if newValue <= 0:
            turns = (abs(newValue) // 100) + (1 if value != 0 else 0)
            value = newValue % 100
            zeroes += turns
        elif newValue > 99:
            turns = (newValue // 100)
            value = newValue % 100
            zeroes += turns
        else:
            value = newValue

    return(zeroes)

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 6)

    def test_real_data(self):
        self.assertEqual(main(False), 6700)

unittest.main()