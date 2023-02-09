from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        visited = set()
        to_visit = deque([ (0,0) ])
        grid[0][0] = 1

        directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        valid = lambda x,y: (
            0 <= x < N and 0 <= y < N
            and grid[x][y] == 0
            and (x,y) not in visited
        )

        while to_visit:
            cur_x, cur_y = to_visit.popleft()
            visited.add((cur_x, cur_y))
            
            distance = grid[cur_x][cur_y]
            if (cur_x, cur_y) == (N-1, N-1):
                return distance
    
            for dx, dy in directions:
                nx, ny = cur_x + dx, cur_y + dy
                if valid(nx, ny):
                    to_visit.append((nx,ny))
                    grid[nx][ny] = min(distance + 1, grid[nx][ny] or 9999)
        return -1

