num1 = int(input())
num2 = int(input())

op = 1 if num1 < num2 else -1

soma = 0
for i in range(num1-1, num2, op):
  if i%2!=0:
    soma+=i
print(soma)