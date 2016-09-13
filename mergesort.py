import sys

def mergeSort(array):

  if len(array) <= 1:
    return array

  mid = len(array)//2
  left = mergeSort(array[mid:])
  right = mergeSort(array[:mid])
  return merge(left, right)


def merge(left, right):

  if not left:
    return right

  if not right:
    return left

  if left[0] > right[0]:
    return [left[0]] + merge(left[1:], right)
  return [right[0]] + merge(left, right[1:])



if __name__ == "__main__":

  print mergeSort([4,5,3])
