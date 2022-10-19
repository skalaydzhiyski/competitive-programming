#!/usr/bin/python3

def runLengthEncoding(s):
  if len(s) == 1: return f'1{s}'
  res = ''
  count = 1
  for i in range(1,len(s)):
    prev, cur = s[i-1], s[i]
    last = i == len(s) - 1
    print(prev, cur, last)
    if prev == cur:
      if count < 9:
        count += 1
      else:
        res += str(count)+prev
        count = 1
    elif prev != cur:
      res += str(count)+prev
      count = 1
    if last:
      res += str(count)+cur
  return res


s = ' '
print(s)
print(runLengthEncoding(s))


