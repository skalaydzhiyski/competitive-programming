class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        current = ""
        for c in s:        
            if c != ' ':
                current += c
                res = current
            else:
                current = ""
        return len(res)
        # return len(s.strip().split()) # better looking but slower 