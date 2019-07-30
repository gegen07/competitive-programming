n = int(input())
arr = list(map(int, input().split()))

mean = sum(arr) / n
squaredDistance = [ (arr[i] - mean)**2 for i in range(n)]
standardDeviation = (sum(squaredDistance) / float(n)) ** (1./2)

print("{0:.1f}".format(standardDeviation))