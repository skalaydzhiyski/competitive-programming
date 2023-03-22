class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            m, revm = {}, {}
            add_word = True
            for charp, char in zip(pattern, word):    
                if charp not in m:
                    m[charp] = char
                    if char in revm and revm[char] != charp:
                        add_word = False
                        break
                    revm[char] = charp
                    continue

                if charp in m and m[charp] != char:
                    add_word = False
                    break
            if add_word:
                res.append(word)
        return res