import random

class MyHashMap(object):
  def __init__(self):
    self.default = []
    self.m = [self.default for _ in range(10**6)]
    self.p = (1<<31) - 1
    self.a, self. b = random.randint(0, self.p-1), random.randint(0, self.p-1)

  def hash(self, key):
    return (self.a * key + self.b) % self.p % len(self.m)

  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: None
    """
    hashkey = self.hash(key)
    self.m[hashkey] = [key,value]

  def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    hashkey = self.hash(key)
    if self.m[hashkey] != self.default:
      return self.m[hashkey][1]
    return -1

  def remove(self, key):
    """
    :type key: int
    :rtype: None
    """
    hashkey = self.hash(key)
    if self.m[hashkey] != self.default:
      self.m[hashkey] = self.default


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
