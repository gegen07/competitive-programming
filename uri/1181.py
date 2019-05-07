line = int(input())
op = input()
mat = [[float(input()) for i in range(12)] for j in range(12)]

soma = 0
cont = 0
for j in range(12):
  soma += mat[line][j]
  cont += 1

if op == 'S':
  print('{:.1f}'.format(soma))
else:
  print('{:.1f}'.format(soma/cont))