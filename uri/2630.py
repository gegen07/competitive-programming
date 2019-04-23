n = int(input())
for i in range(n):
  technique = input()
  R,G,B = map(int, input().split())

  if technique == 'mean':
    print("Caso #{}: {}".format(i+1, int(((R+G+B)/3))))
  elif technique == 'min':
    print("Caso #{}: {}".format(i+1, int(min(R,G,B))))
  elif technique == 'eye':
    print("Caso #{}: {}".format(i+1, int(((0.3*R)+(0.59*G)+(0.11*B)))))
  elif technique == 'max':
    print("Caso #{}: {}".format(i+1, int(max(R,G,B))))
