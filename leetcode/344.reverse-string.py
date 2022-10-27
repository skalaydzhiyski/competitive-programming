class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        for i in range(N//2):
            temp = s[i]
            s[i] = s[N-i-1]
            s[N-i-1] = temp
        
