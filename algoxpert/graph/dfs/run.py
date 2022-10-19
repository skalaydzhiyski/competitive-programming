#!/usr/bin/python3

class Node:
  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  def depthFirstSearch(self, res):
    res.append(self.name)
    for x in self.children:
      x.depthFirstSearch(res)
    return res


