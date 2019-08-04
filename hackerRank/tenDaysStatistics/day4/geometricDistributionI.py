probabilityValues = list(map(int, input().split()))
n = int(input())
probability = probabilityValues[0]/probabilityValues[1]
geometricDistribution = ((1-probability)**(n-1)) * probability
print("{0:.3f}".format(geometricDistribution))