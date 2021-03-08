#!/usr/bin/python3


def solve(a):
  if len(a) == 0: return 1
  a = sorted(a)
  dp = 0
  for x in a:
    if x > dp+1:
      return dp+1
    dp += x
  return dp+1


# what is the minimum amount of change we CANNOT create from the coins given ?
def nonConstructibleChange(coins):
  return solve(coins)

coins = [1,2,5]
#print(nonConstructibleChange(coins))
coins = [1,1,1,1,1]
print(nonConstructibleChange(coins))


