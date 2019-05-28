fat = [1]

def factorial(n):
  if len(fat) <= n:
    for i in range(len(fat), n+1):
      fat.append(fat[i-1]*i)
  return fat[n]

while True:
  try:
    fat1, fat2 = map(int, input().split(' '))
    print(factorial(fat1)+factorial(fat2))  
  except EOFError:
    break