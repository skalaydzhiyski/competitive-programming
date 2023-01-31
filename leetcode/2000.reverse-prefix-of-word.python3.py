class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = word.find(ch)
        if pos == -1:
            return word
        return ''.join(list(reversed(word[:pos+1]))) + word[pos+1:]

