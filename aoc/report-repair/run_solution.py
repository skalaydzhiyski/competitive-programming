#!/usr/bin/python3
import sys
import time

with open('input', 'r') as f:
  inp = [int(x) for x in f.read().split('\n')[:-1]]

a = sorted(inp)
print(a)
print()
size = len(a)
s = 2020

# s-x = sumof any two numbers
d = {s-x: x for x in a}
print(d.keys())
max(d.keys())

for i in range(0, size):
  for j in range(1, size):
    curr = a[i] + a[j]
    if curr in d: 
      print(d[curr]*a[i]*a[j])
      sys.exit(0)




