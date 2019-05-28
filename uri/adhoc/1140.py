while True:
  word = input()
  if word == '*':
    break
  else:
    word = word.lower().split(' ')
    ref = word[0][0]
    isTautogram = True
    for i in range(len(word)):
      if ref != word[i][0]:
        isTautogram = False
        break
    if isTautogram:
      print('Y')
    else:
      print('N')