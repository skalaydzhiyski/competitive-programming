class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        n_store = max(map(max, matches)) + 1
        store = [-1 for _ in range(n_store)]
        for w,l in matches: store[w] = store[l] = 0
        for w,l in matches: store[l] += 1
        left, right = [], []
        for i in range(n_store):
            if store[i] == 0: left.append(i)
            if store[i] == 1: right.append(i)
        return [left, right]