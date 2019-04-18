n = int(input())
while n > 0:
  timeList = [int(j) for j in input().split(" ")]

  differenceTime = 10 
  interval = timeList[0] + 10
  for i in range(1, len(timeList)):
    antInterval = interval
    if timeList[i] < interval:
      interval = timeList[i] + 10 - interval 
      differenceTime += interval
      interval = interval + antInterval
    else:
      interval = timeList[i] + 10
      differenceTime += 10
  print(differenceTime)
  n = int(input())