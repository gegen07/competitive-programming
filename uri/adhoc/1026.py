while True:
  try:
    a, b = map(int, input().split())
    print("{}".format(a^b))
  except EOFError:
    break