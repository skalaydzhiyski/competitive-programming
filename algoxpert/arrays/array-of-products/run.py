#!/usr/bin/python3
from operator import mul
from functools import reduce

def arrayOfProducts(array):
  p, z, zi = 1, 0, 0
  for i,x in enumerate(array):
    if x == 0:
      z += 1
      p *= 1
      zi = i
    else:
      p *= x
  if z > 0:
    res = [0]*len(array)
    res[zi] = 0 if z > 1 else p
  else:
    res = [p//x for x in array]
  return res


#print(arrayOfProducts([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(arrayOfProducts([1, 0, 0, 2, 3]))

