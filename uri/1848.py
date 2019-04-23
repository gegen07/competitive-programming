contYells = 0
sum = 0
while contYells < 3:
  blinkEyes = input()
  if blinkEyes != 'caw caw':
    num = []
    for char in blinkEyes:
      if char == '*':
        num.append('1')
      elif char == '-':
        num.append('0')
    sum += int("".join(num), 2)
  else:
    print(sum)
    sum = 0
    contYells += 1