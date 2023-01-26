from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        graph = defaultdict(set)
        paths = set()
        for left, right in connections:
            graph[left].add(right)
            graph[right].add(left)
            paths.add( (left, right) )

        visited = set()
        def dfs(current, parent):
            if current != 0 and (current, parent) not in paths:
                self.res += 1
                
            visited.add(current)
            for node in graph[current]:
                if node not in visited:
                    dfs(node, current)

        dfs(0, -1)
        return self.res
