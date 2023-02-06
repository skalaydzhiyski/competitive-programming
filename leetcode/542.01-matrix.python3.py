from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        visited = set()
        to_visit = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    to_visit.append( ((i,j), 0) )

        directions = (1,0), (-1,0), (0,1), (0,-1)
        valid = lambda x,y: 0 <= x < m and 0 <= y <n
        while to_visit:
            (i, j), distance = to_visit.popleft()
            for di, dj in directions:
                next_node = (i + di, j + dj)
                if next_node not in visited and valid(*next_node):
                    visited.add(next_node)
                    distance_to_next = distance + 1
                    to_visit.append(
                        (next_node, distance_to_next)
                    )
                    mat[next_node[0]][next_node[1]] = distance_to_next
        return mat