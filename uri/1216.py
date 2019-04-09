distMed = 0
casas = 0
while True:
  try:
    nome = input()
    valor = int(input())
    casas += 1
    distMed += valor 
  except EOFError:
    break
print("{:.1f}".format(distMed/casas))
