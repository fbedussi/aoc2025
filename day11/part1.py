import unittest
from pathlib import Path
from collections import deque

def main(isTest):
    file_name = "test-data.txt" if isTest else "data.txt"
    base_dir = Path(__file__).resolve().parent
    data = {}
    with open(base_dir / file_name) as file:
        for line in file:
            [node, connections] = line.rstrip().split(": ")
            connections = connections.split(' ')
            data[node] = connections
    
    paths = []
    queue = deque([['you']]) 
    while queue:
        path = queue.popleft()
        current_node = path[-1]
        
        if current_node == 'out':
            paths.append(path)
            continue
        
        for neighbor in data[current_node]:
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append(new_path)
    
    return len(paths)


class Test(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(main(True), 5)

    def test_real_data(self):
        self.assertEqual(main(False), 782)


unittest.main()
