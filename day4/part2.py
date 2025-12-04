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
            data.append(list(line.rstrip()))
            
            
    freeRolls = []
    removedRolls = 0

    def isFree(y,x):
        neighboors = [
            [y-1,x-1],
            [y-1,x],
            [y-1,x+1],
            [y,x-1],
            [y,x+1],
            [y+1,x-1],
            [y+1,x],
            [y+1,x+1],
        ]
        rolls = []
        for [y,x] in neighboors:
            if x >= 0 and x < len(data[0]) and y>=0 and y < len(data) and data[y][x] == "@":
                rolls.append([y,x])

        return len(rolls) < 4


    while removedRolls == 0 or len(freeRolls):
        freeRolls = []

        for y in range(0, len(data)):
            for x in range(0,len(data[0])):
                if data[y][x] == "@" and isFree(y,x):
                    freeRolls.append([y,x])
        
        removedRolls += len(freeRolls)
        for [y,x] in freeRolls:
            data[y][x] = "."
            
    
    return(removedRolls)

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 43)

    def test_real_data(self):
        self.assertEqual(main(False), 1397)

unittest.main()