n, c, m = map(int, input().split())
figCarimbadas = list(map(int, input().split()))
figCompradas = list(set(map(int, input().split())))

cont=0
for x in figCarimbadas:
  if x not in figCompradas:
      cont += 1
print(cont)