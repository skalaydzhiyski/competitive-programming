from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [0] * N
        graph = {node: [] for node in range(N)}
        for i in range(N):
            for j in range(i+1, N):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        res = 0
        for node in range(N):
            if visited[node]:
                continue
            to_visit = [node]
            while to_visit:
                current = to_visit.pop()
                visited[current] = 1
                neighbours = [n for n in graph[current] if not visited[n]]
                to_visit += neighbours
            res += 1
        return res
