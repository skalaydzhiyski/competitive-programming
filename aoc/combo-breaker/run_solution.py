#!/usr/bin/python3
from time import time
import matplotlib.pyplot as plt
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


def old(sub, ls, m=d):
  val = 1
  for i in range(ls):
    val *= pow(sub,1, m)
    val *= sub
    val %= m
  return val


# solution 
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
  t0 = time()
  res = old(128, 1000000, d)
  print(time()-t0)
  t0 = time()
  res = f(128, 1000000)
  print(time()-t0)
  t0 = time()
  res = new(128, 1000000,d)
  print(time()-t0)
  
