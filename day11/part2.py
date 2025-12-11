import unittest
from pathlib import Path

# this solution was copied from here:
# https://github.com/MaxArt2501/advent-of-code-2025/blob/main/day-11/part-1-2.js
def count_paths(devices, start, end):
  # Cache that maps devices to the number of paths to the end device
  visited = {}
  
  def walk_path(device):
    if device in visited:
        return visited[device]
    count = 0
    if device in devices:
        for output in devices[device]:
            if output == end:
                count += 1
            else:
                count += walk_path(output)
    else:
        return count
    
    visited[device] = count
    return count
  
  return walk_path(start)


def main(isTest):
    file_name = "test-data2.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    data = {}
    with open(base_dir / file_name) as file:
        for line in file:
            [node, connections] = line.rstrip().split(": ")
            connections = connections.split(' ')
            data[node] = connections
    
    paths = count_paths(data,'svr', 'fft' ) * count_paths(data,'fft', 'dac' )* count_paths(data,'dac', 'out' ) + count_paths(data,'svr', 'dac' ) * count_paths(data, 'dac', 'fft' )* count_paths(data,'fft', 'out' )
    
    return paths


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 2)

    def test_real_data(self):
        self.assertEqual(main(False), 401398751986160)


unittest.main()
