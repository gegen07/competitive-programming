# def percorreColuna(lin, startCol, stopCol, mat, vet, start, reverse=False):
#   if reverse:
#     for i in range(startCol-1, stopCol-1, -1):
#       mat[lin][i] = vet[start]
#       start+=1
#   else:
#     for i in range(startCol, stopCol):
#       mat[lin][i] = vet[start]
#       start+=1
#   return start


# def percorreLinha(col, startLin, stopLin, mat, vet, start, reverse=False):
#   if reverse:
#     for i in range(startLin-1, stopLin-1, -1):
#       mat[i][col] = vet[start]
#       start+=1
#   else:
#     for i in range(startLin, stopLin):
#       mat[i][col] = vet[start]
#       start+=1
#   return start

# lin, col = map(int, input().split())
# vet = [int(i) for i in range(1, (lin*col)+1)]
# mat = [[0 for i in range(col)] for j in range(lin)]

# startVetIndex = 0

# contCol = 1
# contLin = 1

# startLin = 0
# startCol = 0

# stopCol = col
# stopLin = lin

# # startVetIndex = percorreColuna(startLin, startCol, stopCol, mat, vet, startVetIndex)
# # startLin += 1
# # startCol = stopCol-1
# # startVetIndex = percorreLinha(startCol, startLin, stopLin, mat, vet, startVetIndex)
# # startLin, stopLin = stopLin-1, startLin
# # stopCol = 0
# # startVetIndex = percorreColuna(startLin, startCol, stopCol, mat, vet, startVetIndex, True)
# # startCol, stopCol = stopCol, startCol
# # startVetIndex = percorreLinha(startCol, startLin, stopLin, mat, vet, startVetIndex, True)
# # startLin = stopLin
# # startCol += 1
# # startVetIndex = percorreColuna(startLin, startCol, stopCol, mat, vet, startVetIndex)
# # startLin += 1
# # startCol = stopCol-1
# # startVetIndex = percorreLinha(startCol, startLin, stopLin, mat, vet, startVetIndex)
# # startLin, stopLin = stopLin-1, startLin
# # stopCol = 1

# while(True):
#   if contCol % 2 == 0:
#     startVetIndex = percorreColuna(startLin, startCol, stopCol, mat, vet, startVetIndex, True)
#     startCol, stopCol = stopCol, startCol
#   else:
#     startVetIndex = percorreColuna(startLin, startCol, stopCol, mat, vet, startVetIndex)
#     startLin += 1
#     startCol = stopCol-1
#   contCol += 1
#   if startVetIndex == lin*col:
#     break
#   if contLin % 2 == 0:
#     startVetIndex = percorreLinha(startCol, startLin, stopLin, mat, vet, startVetIndex, True)
#     startLin = stopLin
#     startCol += 1
#   else:
#     startVetIndex = percorreLinha(startCol, startLin, stopLin, mat, vet, startVetIndex)
#     startLin, stopLin = stopLin-1, startLin
#     stopCol = contCol-2
#   contLin += 1
#   if startVetIndex == lin*col:
#     break
#   print(mat)
    
# print(mat) 

  
  