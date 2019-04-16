A, G, Ra, Rg = map(float, input().split(" "))

pa = Ra/A 
pg = Rg/G

if pa > pg:
  print('A')
elif pa < pg:
  print('G')
else:
  print('G')