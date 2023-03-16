class Solution:
    def reverseBits(self, n: int) -> int:
        number = bin(n).replace('0b','')
        number = (32-len(number)) * '0' + number
        number = ''.join(list(reversed(number)))
        return int(number, 2)
