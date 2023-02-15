class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        at_exit = lambda x,y: x in (0, m-1) or y in (0, n-1)
        in_bounds = lambda x,y: 0 <= x < m and 0 <= y < n and maze[x][y] != '+'
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        to_visit = deque([ (*entrance, 0) ])
        while to_visit:
            x, y, distance = to_visit.popleft()
            if [x, y] != entrance and at_exit(x, y):
                return distance
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_bounds(nx,ny) and (nx, ny) not in visited:
                    to_visit.append((nx, ny, distance + 1))
                    visited.add((nx,ny))    
        return -1
