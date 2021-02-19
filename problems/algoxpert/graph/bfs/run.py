#!/usr/bin/python3

class Node:
  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  def breadthFirstSearch(self, res):
    res.append(self.name)
    q = self.children
    for x in q:
      res.append(x.name)
      q += x.children
    return res




