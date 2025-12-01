import unittest

def main(isTest):
    fileName = 'test-data.txt' if isTest else 'data.txt'

    data = []
    with open(fileName) as file:
        for line in file:
            if line.strip() == '':
                continue
            number = int(line[1:])
            data.append(number if line[0] == 'R' else -number   )
            
            
    value = 50

    zeroes = 0

    for rotation in data:
        value = (value + rotation) % 100
        if value < 0:
            value = 100 - value
        if value == 0:
            zeroes += 1

    return(zeroes)

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 3)

    def test_real_data(self):
        self.assertEqual(main(False), 1071)

unittest.main()