peca1 = input().split(" ")
peca2 = input().split(" ")

codigo1, numPeca1, valUnit1 = peca1
codigo2, numPeca2, valUnit2 = peca2

print("VALOR A PAGAR: R$ {0:.2f}".format(int(numPeca1) * float(valUnit1) + int(numPeca2) * float(valUnit2)))