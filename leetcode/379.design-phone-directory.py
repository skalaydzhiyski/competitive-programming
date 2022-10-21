
class PhoneDirectory:
  def __init__(self, maxNumbers):
    self.free = set()
    for i in range(maxNumbers):
      self.free.add(i)

  def get(self):
    if len(self.free) == 0:
      return -1
    return self.free.pop()

  def check(self, number):
    return number in self.free

  def release(self, number):
    self.free.add(number)
    


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
