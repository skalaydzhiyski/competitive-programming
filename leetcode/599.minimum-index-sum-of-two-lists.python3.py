from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
            res = defaultdict(list)
            for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[i] == list2[j]:
                        res[(i+j)].append(list1[i])
            return res[min(res.keys())]