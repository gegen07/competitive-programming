n = int(input())
for i in range(n):
  palavra = input().split(' ')
  tam = min(len(palavra[0]), len(palavra[1]))
  string = ""
  for i in range(tam):
    string += palavra[0][i]
    string += palavra[1][i]
  if tam == len(palavra[0]):
    for i in range(tam, len(palavra[1])):
      string += palavra[1][i]
  else:
    for i in range(tam, len(palavra[0])):
      string += palavra[0][i]
  print(string)