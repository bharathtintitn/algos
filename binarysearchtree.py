import sys
import pdb

class Node(object):

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree():
  def __init__(self):
    self.root = None

  def add_node(self, value):

    node = Node(value)
    if self.root == None:
      self.root = node
      return
    else:
      curr = self.root
      prev = self.root
      while curr != None:
        prev = curr
        if curr.value > value:
          curr = curr.left
        else:
          curr = curr.right

      if prev.value < value:
        prev.right = node
        return
      prev.left = node

  def search(self, value):

    curr = self.root
    if not self.root:
      return False
    
    while curr != None:
      if curr.value == value:
        return True
      elif curr.value < value:
        curr = curr.right
      else:
        curr = curr.left

    return False

  def _preOrder(self, root):
      if root == None:
        return
      print root.value
      self._preOrder(root.left)
      self._preOrder(root.right)
      
  def preOrder(self):
      self._preOrder(self.root)


a = BinarySearchTree()
#pdb.set_trace()
a.add_node(10)
a.add_node(8)
a.add_node(12)
a.add_node(6)
a.add_node(11)
a.add_node(13)
a.preOrder()
print a.search(11)
print a.search(10)
print a.search(9)

