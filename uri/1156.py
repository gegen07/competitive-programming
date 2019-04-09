S = 1
numerador = 3
for i in range(1, 20):
  S += (numerador)/(2**i)
  numerador += 2

print("{:.2f}".format(S))