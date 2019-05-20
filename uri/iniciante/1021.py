import math as m

dinheiro = float(input())
dinheiro += 0.001

if dinheiro >= 0 and dinheiro <= 1000000.00:
    frac, intPart = m.modf(dinheiro)

    valoresInt = [100, 50, 20, 10, 5, 2]
    print("NOTAS:")
    for num in valoresInt:
        quantidade = int(intPart-intPart%num)/num
        intPart -= quantidade * num
        print("{0} nota(s) de R$ {1:.2f}".format(int(quantidade), num))

    if intPart == 1:
        frac += 1.00

    valoresFrac = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    print("MOEDAS:")
    for num in valoresFrac:
        if num == 0.01:
            quantidade = round(frac,2) / num
        else:
            quantidade = frac//num
        frac -= quantidade * num
        print("{0} moeda(s) de R$ {1:.2f}".format(int(quantidade), num))