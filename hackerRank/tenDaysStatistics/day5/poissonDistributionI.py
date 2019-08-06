def factorial(x):
  fat = 1

  for i in range(1, x+1):
    fat *= i
  
  return fat

e = 2.71828

pDistribution = lambda mean, k: ((mean ** k) * (e**(-1 * mean)))/factorial(k)

mean = float(input())
k = int(input())

print("{0:.3f}".format(pDistribution(mean, k))) 
