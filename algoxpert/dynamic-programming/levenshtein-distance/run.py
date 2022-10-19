#!/usr/bin/python3


def show(dp):
  for x in dp:
    print(x)
  print("-"*20)


def solve(s1, s2):
  size1, size2 = len(s1)+1, len(s2)+1
  dp = [[x for x in range(size2)]]
  dp += [[x] + [0]*(size2-1) for x in range(1,size1)]
  for i in range(1, size1):
    for j in range(1, size2):
      diag = dp[i-1][j-1] 
      left = dp[i][j-1]
      top  = dp[i-1][j]
      dp[i][j] = min([diag, left, top])+1 if s1[i-1] != s2[j-1] else diag
  show(dp)
  return dp[-1][-1]


def levenshteinDistance(str1, str2):
  return solve(str1, str2)


s1, s2 = 'abc', 'yabd'
print(levenshteinDistance(s1, s2))

s1, s2 = 'biting', 'mitten'
#print(levenshteinDistance(s1, s2))


