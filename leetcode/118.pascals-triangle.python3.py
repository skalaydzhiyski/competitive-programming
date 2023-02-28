class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(1, numRows+1):
            if n < 3:
                res.append( [1]*n ) 
            else:
                inner = [1]
                topleft, topright = res[-1][:-1], res[-1][1:]
                for left, right in zip(topleft, topright):
                    inner.append(left + right)
                inner.append(1)
                res.append(inner)
        return res
