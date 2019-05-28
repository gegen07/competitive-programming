from math import floor

N, M, C = map(int, input().split())
mat = [list(map(int, input().split())) for j in range(N)]
vetVerificaColunas = []

for col in range(M):
  cont0 = 0
  for lin in range(N):
    if mat[lin][col] == 0:
      cont0 += 1 
  if cont0 == N:
    vetVerificaColunas.append(True)
  else:
    vetVerificaColunas.append(False)

isValid = True
for i in range(len(vetVerificaColunas)-1):
  if vetVerificaColunas[i] == False and vetVerificaColunas[i+1] == False:
    isValid = False
    break
if not isValid:
  print("N")
else: 
  isValid = True
  for col in range(M):
    for lin in range(N):
      if mat[lin][col]==1:
        for linVerifica in range(lin+1, lin+C+1):
          if linVerifica < N:
            if mat[linVerifica][col]==1:
              isValid = False
              break
          else:
            break
      elif mat[lin][col]==2:
        for linVerifica in range(lin+1, lin+C+1):
          if linVerifica < N:
            if mat[linVerifica][col]==2:
              isValid = False
              break
          else:
            break
  if isValid:
    print("S")
  else:
    print("N")
