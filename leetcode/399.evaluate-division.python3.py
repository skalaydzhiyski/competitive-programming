from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (left, right), value in zip(equations, values):
            graph[left].append((right, value))
            graph[right].append((left, 1/value))

        res = []
        for start, target in queries:
            if start not in graph.keys():
                res.append(-1)
                continue
                
            found = False
            visited = set()
            to_visit = deque([ (start, 1.) ])
            while to_visit:
                node, current = to_visit.popleft()
                visited.add(node)
                if node == target:
                    res.append(current)
                    found = True
                    break
                for n, val in graph[node]:
                    if n not in visited:
                        visited.add(n)
                        to_visit.append((n, current * val))
            if not found:
                res.append(-1)
        return res