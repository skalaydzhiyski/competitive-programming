from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        res = 0
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            res += 1
            to_visit = [node]
            while to_visit:
                current = to_visit.pop()
                visited.add(current)
                to_visit += [n for n in graph[current] if n not in visited]
        return res