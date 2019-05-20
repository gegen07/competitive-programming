v = [int(i) for i in range(1, int(input())+1)]
qb = [int(i) for i in input().split(' ')]
for x in v:
  if x not in qb:
    print(x)
    break