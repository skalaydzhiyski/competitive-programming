class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_digit_squares(number):
            return sum([int(d)**2 for d in str(number)])

        current = n
        m = set()
        while current not in m:
            s = sum_digit_squares(current)
            if s == 1:
                return True
            m.add(current)
            current = s
        return False
