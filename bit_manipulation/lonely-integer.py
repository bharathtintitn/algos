import sys
import pdb

'''
Consider an array of  integers, , where all but one of the integers occur in pairs. In other words, 
every element in  occurs exactly twice except for one unique element.

Given , find and print the unique element.

Input: 3 --> No element in list
      [1,1,2] --> elements in list

Output: 2

'''

def lonelyInteger(a):
    b = a
    while len(b) > 1:
      #pdb.set_trace()
      element = b.pop(0)
      is_pop = False
      for i in xrange(len(b)):
        if b[i] ^ element == 0:
          b.pop(i)
          is_pop = True
          break

      if not is_pop:
        return element

      #print "list is ",b
    #print "Final list is ",b
    return b[0] 


def lonelyinteger(a):
  return reduce(lambda x,y: x^y, a)


if __name__ == '__main__':

    assert lonelyinteger([1,1,2]) == 2
    assert lonelyinteger([1]) == 1
    assert lonelyinteger([0,0,1,2,1]) == 2
    assert lonelyinteger([4,9,95,93,57,4,57,93,9]) == 95
