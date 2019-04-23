A, B, C = map(float, input().split(" "))
delta = (B**2) - (4*A*C)
if delta >= 0 and A != 0:
  R1 = ((-B) + (delta**(1/2)))/(2*A)
  R2 = ((-B) - (delta**(1/2)))/(2*A)
  print("R1 = {:.5f}\nR2 = {:.5f}".format(R1, R2))
else:
  print("Impossivel calcular")
