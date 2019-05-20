E = 1 
D = 2

while True:
  try:
    n = int(input())
    vet = [[0 for i in range(3)] for j in range(n)] 

    for i in range(n):
      ipt = input().split()
      num = int(ipt[0])
      pe = ipt[1]
      
      if i == 0:
        vet[0][0] = num
        if pe == 'E':
          vet[0][E] += 1
        else: 
          vet[0][D] += 1
      else:
        searched = False
        for k in range(n):
          if vet[k][0] == num:
            vet[k][0] = num
            searched = True
            if pe == 'E':
              vet[k][E] += 1
            else: 
              vet[k][D] += 1
          if searched == True: break
        if searched == False:
          vet[i][0] = num
          searched = True
          if pe == 'E':
            vet[i][E] += 1
          else: 
            vet[i][D] += 1
    par = 0
    for i in range(n):
      par += min(vet[i][E], vet[i][D])
    print("{}".format(par))
  except EOFError:
    break