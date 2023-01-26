from collections import defaultdict

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for node, neighbours in enumerate(rooms):
            graph[node] = [n for n in neighbours if n != node]

        visited = [0 for _ in range(len(rooms))]
        to_visit = [0]
        while to_visit:
            current = to_visit.pop()
            visited[current] = 1
            to_visit += [n for n in graph[current] if not visited[n]]
        return all(visited)
