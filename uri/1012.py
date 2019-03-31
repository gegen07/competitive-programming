valor = input().split(" ")
A, B, C = valor
pi = 3.14159

print("TRIANGULO: {0:.3f}".format((float(A)*float(C))/2))
print("CIRCULO: {0:.3f}".format(pi * float(C) ** 2))
print("TRAPEZIO: {0:.3f}".format(((float(A)+float(B))*float(C))/2))
print("QUADRADO: {0:.3f}".format((float(B)**2)))
print("RETANGULO: {0:.3f}".format((float(A)*float(B))))