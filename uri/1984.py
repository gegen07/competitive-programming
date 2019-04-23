word = int(input())
word = str(word)
for char in range(len(word)-1, -1, -1):
  print(int(word[char]), end='')
print()