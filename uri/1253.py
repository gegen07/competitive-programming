alfa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n = int(input())
for i in range(n):
  palavra = list(input())
  casas = int(input())
  for i in range(len(palavra)):
    palavra[i] = alfa[alfa.index(palavra[i])-casas]
  print(str("".join(palavra)))