#!/usr/bin/python3
from collections import Counter 
from itertools import chain


mapping = dict(zip('abcdefghijklmnopqrstuvwxyz', list(range(1, 27))))

def value(s):
  if len(s) == 1:
    return mapping[s]
  return mapping[s[0]] + value(s[1:])

def substrings(s):
  return [] if len(s) == 0 else [s] + substrings(s[1:])

def group(s):
  res = []
  current = []
  for c in s:
    if len(current) == 0 or c == current[-1]:
      current.append(c)
    else:
      res.append(current)
      current = [c]
  return res + [current]


def solve(q):
  def joiner(lst): return ''.join(lst)
  res = set(list(map(joiner, group(s))))
  res = list(chain.from_iterable([substrings(g) for g in res]))
  res = [value(x) for x in res]
  return "Yes" if q in res else "No"


s = input()
n = int(input())
for _ in range(n):
  q = int(input())
  print(solve(q))


