#!/usr/bin/python3

'''
 Given N steps, return how many different ways
 there are to climb them using memoization and 
 dynamic programming techniques
''' 


class Solution:
    def climbStairs(self, n: int) -> int:
      res = 0
      dp = [1,1]
      for x in range(2, n):
        dp.append(dp[x-1] + dp[x-2])
      return dp[-1]


if __name__ == '__main__':
  n = 5
  sol = Solution()
  print(sol.climbStairs(n))

