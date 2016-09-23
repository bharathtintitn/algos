import sys

'''
  Finding all combinations of well formed brackets.
  Valid Permutaion of parenthesis.

  Eg: ()(), (()) --> n = 2
      ((())), (())(), ()()(), ()(()) --> n = 3

'''

def parenthesis(n):

  _parenthesis("",0,0,n)


def _parenthesis(string, openCount, closeCount, n):

  if openCount == n and closeCount == n:
    print string

  else:

    if openCount < n:
      _parenthesis(string + '(', openCount + 1, closeCount, n)

    if closeCount < openCount:
      _parenthesis(string + ')', openCount, closeCount + 1, n)


if __name__ == "__main__":

  parenthesis(2)
  parenthesis(3)
