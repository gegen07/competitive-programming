def median(arr, lengthArr):
  if arr == None:
    return None

  median = None

  if (lengthArr % 2 == 0):
    median = (arr[(lengthArr//2)-1] + arr[lengthArr//2]) // 2
  else:
    median = arr[lengthArr//2]
  
  return median

def partitions(arr, lengthArr):
  firstPartition = None
  secondPartition = None
  thirdPartition = None

  if (lengthArr % 2 == 0):
    firstPartition = arr[:lengthArr//2]
    secondPartition = median(arr, lengthArr)
    thirdPartition = arr[lengthArr//2:]
  else:
    firstPartition = arr[:(lengthArr//2)]
    secondPartition = median(arr, lengthArr)
    thirdPartition = arr[(lengthArr//2)+1:]

  return firstPartition, secondPartition, thirdPartition

lengthArr = int(input())
arr = list(map(int, input().split()))
arr.sort()

partsArr = list(partitions(arr, lengthArr))
quartile1 = median(partsArr[0], len(partsArr[0]))
quartile2 = partsArr[1]
quartile3 = median(partsArr[2], len(partsArr[2]))

print("{0}\n{1}\n{2}".format(quartile1, quartile2, quartile3))