while True:
  try:
    n = int(input())
    cM, cL = map(int, input().split())
    matM = [list(map(int, input().split())) for j in range(cM)]
    matL = [list(map(int, input().split())) for j in range(cL)]

    ecM, ecL =  map(int, input().split())
    at = int(input())

    if matM[ecM-1][at-1] > matL[ecL-1][at-1]:
      print("Marcos")
    elif matM[ecM-1][at-1] < matL[ecL-1][at-1]:
      print("Leonardo")
    else:
      print("Empate")
  except EOFError:
    break