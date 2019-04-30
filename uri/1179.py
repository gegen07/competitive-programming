vImpar = []
vPar = []
for i in range(15):
  x = int(input())
  if x % 2 == 0:
    vPar.append(x)
  else:
    vImpar.append(x)
  if len(vPar) == 5:
    for i in range(len(vPar)):
      print("par[{}] = {}".format(i, vPar[i]))
    vPar = []
  if len(vImpar) == 5:
    for i in range(len(vImpar)):
      print("impar[{}] = {}".format(i, vImpar[i]))
    vImpar=[]
for i in range(len(vImpar)):
  print("impar[{}] = {}".format(i, vImpar[i]))
for i in range(len(vPar)):
  print("par[{}] = {}".format(i, vPar[i]))