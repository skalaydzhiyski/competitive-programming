from collections import deque

class Solution:
    def minMutation(self, start: str, target: str, bank: List[str]) -> int:
        get_distance = lambda left, right: sum([l != r for l,r in zip(left, right)])
        visited = set()
        to_visit = deque([ (start, 0) ])
        while to_visit:
            current, distance = to_visit.popleft()
            print(current)
            if current == target:
                return distance
            for gene in bank:
                if get_distance(current, gene) == 1 and gene not in visited:
                    visited.add(gene)
                    to_visit.append((gene, distance + 1))
        return -1

