import pdb

def quickSort(array, start, end):
  '''
  Algorithm to sort given array in 
  ascending order.
  '''
 
  if start < end:
    mid = pivot(array, start, end)
    quickSort(array, start, mid - 1)
    quickSort(array, mid + 1, end)

  print "Final sorted array is ", array


def pivot(array, start, end):
  '''
  Here we place first element to its position.
  '''

  low = start + 1
  high = end
  if start < end:
    element = array[start]
  while low < high:

    while low < high and array[low] < element:
      low += 1

    while array[high] > element and high > low:
      high -= 1

    if low > high:
      array[low], array[high] = array[high], array[low]


  #pdb.set_trace()
  array[low], array[start] = array[start], array[low]
  return low

def main():

  array = [10, 4 , 8, 5, 2, 9, 0, 7]
  #array = [10, 4 , 8, 5]
  #pdb.set_trace()
  quickSort(array, 0, 7)


if __name__=="__main__":

  main()
