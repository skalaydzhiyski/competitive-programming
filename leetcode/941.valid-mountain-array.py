class Solution:
  def validMountainArray(self, arr):
    N = len(arr)
    if N < 3: return False
    
    peaks, valleys, flats = 0, 0, 0
    for i in range(1, N-1):
      prev, current, next = arr[i-1], arr[i], arr[i+1]
      if prev < current > next:
        peaks += 1
      if prev > current < next:
        valleys += 1
      if prev == current or next == current:
        flats += 1
    
    return peaks == 1 and valleys == 0 and flats == 0

