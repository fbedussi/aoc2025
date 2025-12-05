import unittest
from pathlib import Path

def main(isTest):
    file_name = 'test-data.txt' if isTest else 'data.txt'
    base_dir = Path(__file__).resolve().parent
    ranges = []
    with open(base_dir / file_name) as file:
        for line in file:
            if line.rstrip() == '':
                break
            else:
                [start, end] = line.rstrip().split('-') 
                ranges.append([int(start), int(end)])
            
    def merge_ranges():
        for [min, max] in ranges:
            modified = False
            for index, [min_m, max_m] in enumerate(merged_ranges):
                if min >= min_m and max <= max_m:
                    modified = True
                    break
                elif min >= min_m and min <= max_m and max > max_m:
                    merged_ranges[index][1] = max
                    modified = True
                    break

                elif max <= max_m and max >= min_m and min < min_m:
                    merged_ranges[index][0] = min
                    modified = True
                    break

                elif min <= min_m and max >= max_m:
                    merged_ranges[index] = [min, max]
                    modified = True
                    break

            if not modified:
                merged_ranges.append([min, max])


    merged_ranges = []
    merge_ranges()
    while (len(merged_ranges) != len(ranges)):
        ranges = merged_ranges
        merged_ranges = []
        merge_ranges()
                
    number_of_ids = 0
    for [min, max] in merged_ranges:
        number_of_ids += max-min+1
    
    return(number_of_ids)

class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 14)

    def test_real_data(self):
        self.assertEqual(main(False), 360341832208407)

unittest.main()