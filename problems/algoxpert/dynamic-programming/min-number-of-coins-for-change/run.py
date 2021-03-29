#!/usr/bin/python3

def solve(a, t):
  m = 999999
  dp = [0] + [m]*(t)
  for x in a:
    if x > t: continue
    for i in range(x, len(dp)):
      dp[i] = min(dp[i], dp[i-x]+1)
  res = dp[-1]
  return res if res != m else -1

def minNumberOfCoinsForChange(t, a):
  return solve(a, t)

t = 7
a = [1,5,10]
print(minNumberOfCoinsForChange(t, a))

t = 3
a = [2,1]
print(minNumberOfCoinsForChange(t, a))

t = 9
a = [3,5]
print(minNumberOfCoinsForChange(t, a))

t = 10
a = [3,4]
print(minNumberOfCoinsForChange(t, a))
