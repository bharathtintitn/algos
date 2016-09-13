import sys
import pdb

class Node(object):

  def __init__(self):
    self.is_end = False
    self.string = None
    self.alphabets = {}


class Tries(object):

  def __init__(self):
    self.root = None

  def add(self, string):

    if self.root == None:
      node = Node()
      self.root = node

    curr = self.root
    prev = curr

    if len(string) > 0:
      print "String is ",string

      for i in string:
        if i not in curr.alphabets:
          node = Node()
          curr.alphabets[i] = node
        curr = curr.alphabets[i]

      curr.string = string


  def search(self, string):

    curr = self.root

    for i in string:
      if curr != None and i in curr.alphabets:
        curr = curr.alphabets[i]
      else:
        return False

    return True


if __name__ == "__main__":

  a = Tries()
  a.add('abc')
  a.add('acd')
  #pdb.set_trace()
  print a.search('abc')
  print a.search('ab')
  print a.search('a')
  print a.search('ac')


