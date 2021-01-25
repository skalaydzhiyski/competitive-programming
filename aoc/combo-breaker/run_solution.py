#!/usr/bin/python3
from time import time
with open("input") as f:
  res = f.read()
inp = res.split('\n')[:-1]
#------------------------------

# test case
#pkc, pkd = 5764801,17807724
pkc, pkd = inp
pkc, pkd = int(pkc), int(pkd)
d = 20201227
sub = 7

def f(sub, ls):
  return pow(sub, ls, d)

def run():
  lsc = 1
  while f(sub, lsc) != pkc:
    lsc += 1
  print(lsc)

  lsd = 1
  while f(sub, lsd) != pkd:
    lsd += 1
  print(lsd)

  res = f(pkc, lsd)
  print(res, lsc, lsd)

if __name__ == '__main__':
  run()
  

