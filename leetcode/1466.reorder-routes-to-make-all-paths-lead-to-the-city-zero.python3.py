from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        paths = set()
        for left, right in connections:
            graph[left].add(right)
            graph[right].add(left)
            paths.add( (left, right) )

        res = 0
        visited = set()
        to_visit = [(0, -1)]
        while to_visit:
            current, parent = to_visit.pop()
            visited.add(current)
            if current != 0 and (current, parent) not in paths:
                res += 1
            to_visit += [
                (node, current) 
                for node in graph[current]
                if node not in visited
            ]
        return res
