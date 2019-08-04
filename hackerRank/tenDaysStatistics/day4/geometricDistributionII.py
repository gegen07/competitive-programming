probabilityValues = list(map(int, input().split()))
n = int(input())
probability = probabilityValues[0]/probabilityValues[1]

geometricDistribution = lambda n : ((1-probability)**(n-1)) * probability

result = sum(map(geometricDistribution, range(1, 6)))

print("{0:.3f}".format(result))