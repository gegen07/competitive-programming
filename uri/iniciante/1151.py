a = 0
b = 1
fib = 0
interval = int(input())
for i in range(interval):
  if i == interval - 1:
    print(fib)
  else: 
    print(fib, end=" ")
    fib = a+b
    b = a
    a = fib