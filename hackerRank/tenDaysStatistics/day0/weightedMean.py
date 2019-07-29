len = int(input())
arrNumbers = list(map(int, input().split()))
arrWeight = list(map(int, input().split()))

dividend = 0
for i in range(len):
  dividend += arrNumbers[i]*arrWeight[i]

weightedMean = dividend/sum(arrWeight)

print("{0:.1f}".format(weightedMean))