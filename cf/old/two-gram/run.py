#!/usr/bin/python3
import operator

n = int(input())
s = input()

res = {}
for i in range(len(s)-1):
  key = s[i]+s[i+1]
  if key in res:
    res[key] += 1
  else:
    res[key] = 1

print(max(res.items(), key=operator.itemgetter(1))[0])


