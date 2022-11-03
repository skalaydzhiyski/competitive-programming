class Solution:
    def countElements(self, arr: List[int]) -> int:
        # TODO: continue here when you're coming back to coding.
        m = set(arr)
        res = 0
        for x in arr:
            if x + 1 in m:
                res += 1
        return res
