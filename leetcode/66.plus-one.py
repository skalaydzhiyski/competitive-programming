class Solution:
  def plusOne(self, digits):
    for i in range(len(digits)-1, -1, -1):
      print(digits[i])
      if digits[i]+1 > 9:
        digits[i] = 0
        if i == 0:
          digits = [1] + digits
      else:
        digits[i] += 1
        break
    return digits
