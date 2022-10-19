#!/usr/bin/python3

def solve(a, t):
  dp = [1] + [0]*t
  for x in a:
    for i,d in enumerate(dp):
      if x <= i:
        dp[i] += dp[i-x]
  return dp[-1]


def numberOfWaysToMakeChange(t, a):
  return solve(a, t)

t = 10
a = [1, 5, 10, 25]
print(numberOfWaysToMakeChange(t, a))

