Alice, Bea = map(int, input().split())
while(Alice != 0 and Bea != 0):
  setAlice = set()
  setBea = set()
  
  for x in list(map(int, input().split())):
    setAlice.add(x)    

  for x in list(map(int, input().split())):
    setBea.add(x)

  total = 0

  if len(setAlice) < len(setBea):
    total = setAlice.difference(setBea)
  else:
    total = setBea.difference(setAlice)
  print(len(total))

  Alice, Bea = map(int, input().split())
