valores = input().split(" ")
M = int(valores[0])
N = int(valores[1])

while M > 0 and N > 0:
  seq = []
  if M > N:
    for i in range(N, M+1):
      seq.append(i)
  elif M < N:
    for i in range(M, N+1):
      seq.append(i)
  else:
    seq.append(0) 

  soma = 0
  for i in seq:
    soma+=i

  print(*seq, end=" ")
  print("Sum={}".format(soma))
  
  valores = input().split(" ")
  M = int(valores[0])
  N = int(valores[1])
