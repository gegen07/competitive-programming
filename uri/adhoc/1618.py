n = int(input())
for i in range(n):
  Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, Rx, Ry = map(int, input().split())
  if (Rx >= Ax and Rx <= Bx) and (Ry >= Ay and Ry <= Cy):
    print(1)
  else:
    print(0)