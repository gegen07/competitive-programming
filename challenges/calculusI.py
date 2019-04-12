a = []

def f(x):
  return eval(func)
def angularCoeficientTangentCres(x0, x1):
  if abs(x0-x1) > 0:
    y1 = f(x1)
    y0 = f(x0)
    a.append(round((y1 - y0) / (x1 - x0), 3))
    angularCoeficientTangentCres(x0, round(x1-0.01, 3))
  else: 
    return

def angularCoeficientTangentDecres(x0, x1):
  if abs(x1-x0) > 0:
    y1 = f(x1)
    y0 = f(x0)
    a.append(-1.*round((y1 - y0) / (x1 - x0), 3))
    angularCoeficientTangentDecres(x0, round(x1+0.01, 3))
  else: 
    return

func = input()
x0, x1 = map(float, input().split(" "))

if max(x0, x1) == x1: 
  angularCoeficientTangentCres(x0, x1)
  print(a[len(a)-1])
else:
  angularCoeficientTangentDecres(x0, x1)
  print(a[len(a)-1])