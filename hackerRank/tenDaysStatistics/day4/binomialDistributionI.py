def factorial(x):
  fat = 1

  for i in range(1, x+1):
    fat *= i
  
  return fat


def binomialDistribution(x, n, p):
  combination = factorial(n) / (factorial(x)*(factorial(n-x)))
  return (combination) * (p**x) * ((1-p)**(n-x))

values = list(map(float, input().split()))

p = values[0]/(values[0] + values[1])
n = 6

cumulativeProbability = 0

for i in range(n//2, n+1):
  cumulativeProbability += binomialDistribution(i, n, p)

print("{0:.3f}".format(cumulativeProbability))