def validCol(mat, col):
  countingArr = []
  isValid = True

  for j in range(9):
    countingArr.append(mat[j][col])
  for l in range(1,10):
    if countingArr.count(l) != 1:
      isValid = False
      break

  return isValid
  
def validLin(mat, lin):
  countingArr = []
  isValid = True

  for i in range(9):
    countingArr.append(mat[lin][i])

  for l in range(1,10):
    if countingArr.count(l) != 1:
      isValid = False
      break
  return isValid

n = int(input())
matInstance = [[list(map(int, input().split(' '))) for j in range(9)] for i in range(n)]
validArr = [True for i in range(n)]
countingArr = []

for i in range(n):
  startLin = 0
  stopLin = 3
  while startLin != 9:
    isValid = True
    startCol = 0
    stopCol = 3
    while startCol != 9:
      for j in range(startLin, stopLin):
        for k in range(startCol, stopCol):
          countingArr.append(matInstance[i][j][k])
      for l in range(1,10):
        if countingArr.count(l) != 1:
          isValid = False
          break
      countingArr = []
      if isValid == False:
        validArr[i] = False
        break
      startCol += 3
      stopCol += 3
    startLin += 3
    stopLin += 3

countingArr = []
for i in range(n):
  for j in range(9):
    if validArr[i] == True:
      validArr[i]=validLin(matInstance[i], j)
    for k in range(9):
      if validArr[i] == True:
        validArr[i]=validCol(matInstance[i], k)
      
for i in range(n):
  print("Instancia {}".format(i+1))
  print("{}".format("SIM" if validArr[i] else "NAO"))
  print()
