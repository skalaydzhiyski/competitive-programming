#!/usr/bin/python3


def solve(red, blue):
  red = sorted(red)
  blue = sorted(blue)
  
  res_blue, res_red = 0,0
  for x,y in zip(red, blue):
    if x>y: res_red += 1
    if x<y: res_blue += 1
  return res_blue == len(blue) or res_red == len(blue)


def classPhotos(redShirtHeights, blueShirtHeights):
  return solve(redShirtHeights, blueShirtHeights)


blue = [5,8,1,3,4]
red = [6,9,2,4,5]
print(classPhotos(red, blue))


