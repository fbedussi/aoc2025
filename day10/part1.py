import unittest
from pathlib import Path
from itertools import combinations


def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    data = []
    with open(base_dir / file_name) as file:
        for line in file:
            parts = line.rstrip().split(" ")
            lights = list(parts[0][1:-1])
            buttons = list(map(lambda button:list(map(int, button[1:-1].split(','))), parts[1:-1]))
            joltage = parts[-1][1:-1].split(',')
            data.append([lights, buttons, joltage])

    def solves(expected, combo):
        actual = ['.'] * len(expected)
        for button in combo:
            for i in button:
                actual[i] = '#' if actual[i] == '.' else '.'
                
        return ''.join(expected) == ''.join(actual)
    
    def get_min_pressures(d):
        expected = d[0]
        buttons = d[1]
        pressures = None

        all_combinations = []
        for r in range(1, len(buttons) + 1):
            all_combinations.extend(combinations(buttons, r))

        for combo in all_combinations:
            if solves(expected, combo):
                pressures = len(combo)
                break
        
        

        return pressures
    
    min_pressures = list(map(get_min_pressures, data))
    
    return sum(min_pressures)


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 7)

    def test_real_data(self):
        self.assertEqual(main(False), 438)


unittest.main()
