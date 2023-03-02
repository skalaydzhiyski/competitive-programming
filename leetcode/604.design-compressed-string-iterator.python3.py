class StringIterator:
    def __init__(self, compressedString: str):
        self.current = 0
        if len(compressedString) == 1:
            self.s = compressedString
        else:
            digits = '1234567890'
            res = ""
            current = compressedString[0]
            count = ""
            for x in compressedString[1:]:
                if x in digits:
                    count += x
                else:
                    res += current * int(count)
                    current = x
                    count = ""
            res += current * int(count)
            self.s = res


    def next(self) -> str:
        if self.current < len(self.s):
            res = self.s[self.current]
            self.current += 1
            return res
        return " "

    def hasNext(self) -> bool:
        return self.current < len(self.s)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
