class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        res = []
        for word in words:
            for s in [first, second, third]:
                chars = set(s) | set(word.lower())
                if len(chars) ==  len(s):
                    res.append(word)
        return res

