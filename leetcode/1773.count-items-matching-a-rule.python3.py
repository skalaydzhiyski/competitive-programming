class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for type_, color_, name_ in items:
            if ruleKey == 'type':
                if type_ == ruleValue:
                    res += 1
            elif ruleKey == 'color':
                if color_ == ruleValue:
                    res += 1
            elif ruleKey == 'name':
                if name_ == ruleValue:
                    res += 1
        return res
