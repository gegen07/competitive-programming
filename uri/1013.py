def maxValue(a,b):
    return ((a+b+abs(a-b))/2)

valores = input().split(" ")
A, B, C = valores

print("{0} eh o maior".format(int(maxValue(maxValue(int(A), int(B)), int(C)))))