def factorial(x):
  fat = 1

  for i in range(1, x+1):
    fat *= i
  
  return fat


def binomialDistribution(x, n, p):
  combination = factorial(n) / (factorial(x)*(factorial(n-x)))
  return (combination) * (p**x) * ((1-p)**(n-x))

values = list(map(float, input().split()))

p = values[0]/100
n = 10

cumulativeProbability1 = cumulativeProbability2 = 0

for r in range(0, 3):
  cumulativeProbability1 += binomialDistribution(r, n, p)

for r in range(2, n+1):
  cumulativeProbability2 += binomialDistribution(r, n, p)

print("{0:.3f}\n{1:.3f}".format(cumulativeProbability1, cumulativeProbability2))