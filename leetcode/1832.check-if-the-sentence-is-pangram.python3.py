class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        abet = {chr(x) for x in range(97, 123)}
        res = set()
        for c in sentence:
            res.add(c)
        return len(res) == len(abet)
