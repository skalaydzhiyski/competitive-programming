class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        right, left = 0, 0
        for direction, size in shift:
            if direction == 0:
                right += size
            else:
                left += size

        shift = (right - left) % len(s)
        res = s[shift:] + s[:shift]
        return res
