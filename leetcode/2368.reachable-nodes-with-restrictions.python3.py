from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        res = 0
        visited = set(restricted)
        to_visit = [0]
        while to_visit:
            current = to_visit.pop()
            if current not in visited:
                res += 1
            visited.add(current)
            to_visit += [
                n for n in graph[current]
                if n not in visited
            ]
        return res