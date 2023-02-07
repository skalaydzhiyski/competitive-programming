class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for chars in zip(*strs):
            if len(set(chars)) != 1:
                return res
            res += chars[0]
        return res
