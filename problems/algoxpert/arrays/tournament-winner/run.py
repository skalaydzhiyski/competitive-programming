#!/usr/bin/python3

from time import time 

def solve(comp, results):
  res = ""
  d = {t:0 for t in set([x for sublist in comp for x in sublist])}
  print(d)
  for match, score in zip(comp, results):
    d[match[abs(score-1)]] += 1
  return max(d, key=d.get)



def tournamentWinner(competitions, results):
  # Write your code here.
  return solve(competitions, results)


competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]
print(tournamentWinner(competitions, results))

