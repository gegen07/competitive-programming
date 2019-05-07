lin, col = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(lin)]
somaLin = 0
somaCol = 0
maiorSoma = 0
for i in range(lin):
  for j in range(col):
    somaLin += mat[i][j]
    for k in range(lin):
      somaCol += mat[k][j]
    if somaCol > maiorSoma:
      maiorSoma = somaCol
    somaCol = 0
  if somaLin > maiorSoma:
    maiorSoma = somaLin
  somaLin = 0
print(maiorSoma)