from math import floor
import random

class MyHashSet(object):

  def __init__(self):
    self.set = [[] for _ in range(1<<10)]
    self.p = (1<<31) - 1 # INT_MAX
    self.a, self.b = random.randint(0, self.p-1), random.randint(0, self.p-1)
    self.w = 20
  
  def hash(self, key):
    return ((self.a * key + self.b) % self.p) % len(self.set)

  # O(1)
  def add(self, key):
    """
    :type key: int
    :rtype: None
    """
    hashkey = self.hash(key)
    if key not in self.set[hashkey]:
      self.set[hashkey].append(key)
    
  # O(1)
  def remove(self, key):
    """
    :type key: int
    :rtype: None
    """
    hashkey = self.hash(key)
    if key in self.set[hashkey]:
      self.set[hashkey].remove(key)
    

  # O(1)
  def contains(self, key):
    """
    :type key: int
    :rtype: bool
    """
    return key in self.set[self.hash(key)]


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
print(obj.set)
obj.add(1)
obj.add(2)
obj.add(3)
print(obj.set)
print(obj.hash(128))
