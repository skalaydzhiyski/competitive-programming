from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for left, right in edges:
            graph[left].add(right)
            graph[right].add(left)

        visited = set()
        to_visit = [source]
        while to_visit:
            current = to_visit.pop()
            visited.add(current)
            if current == destination:
                return True
            to_visit += [n for n in graph[current] if n not in visited]
        return False
