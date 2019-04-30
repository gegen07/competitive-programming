n = int(input())
while n > 0:
  v = [int(i) for i in input().split(' ')]
  decresc = False
  cresc = False
  pico = 0
  for i in range(len(v)):
    if i != 0 :
      if v[i-1] < v[i] and cresc == True:
        cresc = False
        decresc = True
        pico += 1
      elif v[i-1] > v[i] and decresc == True:
        cresc = True
        decresc = False
        pico += 1
    else:
      if v[len(v)-1] > v[i]:
        cresc = True
      else:
        decresc = True
  if v[len(v)-1] < v[0] and cresc == True:
    pico += 1
  elif v[len(v)-1] > v[0] and decresc == True:
    pico += 1
  print(pico)
  n = int(input())