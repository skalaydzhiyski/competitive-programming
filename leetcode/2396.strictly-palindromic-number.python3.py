class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def in_base(x, b):
            res = []
            while x:
                c = x % b
                x //= b
                res.append(c)
            return res

        def is_palindrome(lst):
            size = len(lst)
            for left in range(0, size):
                right = size-left-1
                if lst[left] != lst[right]:
                    return False
                if left == right:
                    break
            return True

        res = True
        for base in range(2, n-1):
            res &= is_palindrome(in_base(n, base))
        return res
