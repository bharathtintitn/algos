
def binary_search(array, item):
  '''
  Algorithm to serach an elemnt.
  '''

  length = len(array)
  print 'length ',length
  if length <= 0:
    print "No element to search in array"
    return

  low = 0
  high = length - 1
  #print "low is ",low,"high is ",high

  while(low < high):

    mid = (low + high)/2

    print 'mid is ',mid

    if array[mid] == item:
      print "item is present"
      return
    elif array[mid] > item:
      high = mid - 1
    elif array[mid] < item:
      low = mid + 1

    #print "low is ",low,"high is ",high

  print "Item is not present"





def main():

  array = [1, 2, 3, 4, 5, 6,7,8,9,10]
  binary_search(array, 8)
  binary_search(array, 13)
  binary_search(array, 5)
  binary_search(array, 0)

if __name__=="__main__":
  main()
