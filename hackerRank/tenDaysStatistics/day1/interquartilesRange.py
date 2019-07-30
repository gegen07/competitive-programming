def median(arr, lengthArr):
  if arr == None:
    return None

  median = None

  if (lengthArr % 2 == 0):
    median = (arr[(lengthArr//2)-1] + arr[lengthArr//2]) / 2.
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
arrFreq = list(map(int, input().split()))

dataset = []

for i in range(lengthArr):
  for j in range(arrFreq[i]):
    dataset.append(arr[i])    

dataset.sort()

partsArr = list(partitions(dataset, len(dataset)))
quartile1 = median(partsArr[0], len(partsArr[0]))
quartile3 = median(partsArr[2], len(partsArr[2]))

print("{0:.1f}".format(quartile3 - quartile1))