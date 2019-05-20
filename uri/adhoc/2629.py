import itertools
def multPermutation(perm, mat, sf, sl):
  lst = list(map(int, str(sf) + "".join(str(e) for e in perm) + str(sl)))
  mult = 1
  vet = []
  
  for i in range(len(lst)-1):
    vet.append([lst[i], lst[i+1]]) 

  for i in range(len(vet)):
    mult *= mat[vet[i][1]-1][vet[i][0]-1]
  return mult

while True:
  try:
    n = int(input())
    mat = [list(map(float, input().split())) for j in range(n)]

    probabilityShow = int(input())
    probabilityShowMat = [list(map(int, input().split())) for j in range(probabilityShow)]
    for i in range(probabilityShow):
      sum = 0
      perm = list("".join(str(e) for e in range(1,n+1)))
      for p in itertools.product(perm, repeat=probabilityShowMat[i][2]-1): 
        sum += multPermutation(p, mat, probabilityShowMat[i][0], probabilityShowMat[i][1])
      print("{:.6f}".format(sum)) 
  except EOFError:
    break