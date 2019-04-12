# Developed by DenerRibeiro
def f(x):
  return eval(func)


def average(x, dx):
  # limit in x+ => ap (angular coeficient plus)
  ap = (f(x+dx) - f(x)) / (dx)

  # limit in x- => am (angular coeficint minus)
  am = (f(x) - f(x-dx)) / (dx)

  return (ap+am)/2

func = input("function: ")
x0 = float(input("tangent at: "))
dx = float(input("precision: "))
a = average(x0, dx)
b = f(x0) - (a * x0)

print("t(x) = {}x + {}".format(a, b))