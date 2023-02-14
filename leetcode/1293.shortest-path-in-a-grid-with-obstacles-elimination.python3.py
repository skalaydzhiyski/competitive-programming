from collections import deque

class Solution:
    '''
    NOTE:
        For this problem, there are 2 things to notice:
        1. As per BFS invariant -> the first path to reach the target is the shortest!
        2. Following up from (1) -> we need to visit all paths in the graph
            and keep track of what we have visited as a state = (position, k)
            so that we don't visit the same position with the same value of k
            which is unnecessary due to BFS property from (1).
    '''
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        mdist = m + n - 2
        if k >= mdist:
            return mdist

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        in_bounds = lambda x,y: 0 <= x < m and 0 <= y < n
        visited = set()
        to_visit = deque([ ((0,0,k), 0) ])
        target = (m-1, n-1)

        while to_visit:
            (curr_x, curr_y, curr_k), distance = to_visit.popleft()
            if (curr_x, curr_y) == target:
                return distance

            for dx, dy in directions:
                nx, ny = curr_x + dx, curr_y + dy
                if not in_bounds(nx, ny):
                    continue

                nk = curr_k - grid[nx][ny]
                next_state = (nx, ny, nk)
                if nk >= 0 and next_state not in visited:
                    visited.add(next_state)
                    to_visit.append( (next_state, distance + 1) )
        return -1


