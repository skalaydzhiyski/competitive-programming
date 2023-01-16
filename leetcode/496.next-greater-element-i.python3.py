class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {k:-1 for k in nums1}
        stack = []
        for current in nums2:
            if stack and current <= stack[-1]:
                stack.append(current)
                continue
            while stack and current > stack[-1]:
                x = stack.pop()
                if x in m:
                    m[x] = current
            stack.append(current)
        return m.values()