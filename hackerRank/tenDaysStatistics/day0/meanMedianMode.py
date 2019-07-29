len = int(input())
arr = list(map(float, input().split()))

# mean
mean = sum(arr) / len

# mode
count, mode = 0, arr[0]
for x in arr:
  if arr.count(x) == count:
    if mode > x:
      mode = x
  elif arr.count(x) > count:
    count = arr.count(x)
    mode = x

# median
arr.sort()
middle = len // 2
median = (arr[middle] + arr[middle-1]) / 2

print("{0:.1f}\n{1:.1f}\n{2:.1f}".format(mean, median, mode))