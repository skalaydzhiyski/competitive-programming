#!/usr/bin/python3
from collections import Counter
from itertools import combinations


def check(s):
  return not any([s[i] == s[i+1] for i in range(len(s)-1)])


def solve(s):
  res = -1
  unq = set(s)
  counts = Counter(s)
  combs = list(combinations(set(s), 2))
  for comb in combs:
    toRemove = unq - set(comb)
    new = ''.join([x for x in s if x not in toRemove])
    if check(new):
      res = max(res, len(new))
  return res

s = "beabeefeab"
res = solve(s)
print(res)



