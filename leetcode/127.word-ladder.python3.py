from collections import deque, defaultdict
import string

class Solution:
    # NOTE: There is a solution with BiDirectional BFS, but that is outside current scope.
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        m = defaultdict(list)
        N = len(beginWord)
        for word in wordList:
            for i in range(N):
                pattern = word[:i] + '*' + word[i+1:]
                m[pattern].append(word)

        visited = set([beginWord])
        to_visit = deque([ (beginWord, 1) ])
        while to_visit:
            current, distance = to_visit.popleft()
            if current == endWord:
                return distance

            for i in range(N):
                pattern = current[:i] + '*' + current[i+1:]
                for word in m[pattern]:
                    if word not in visited:
                        visited.add(word)
                        to_visit.append( (word, distance + 1) )
        return 0
