w1=w2=r=-1
medias = 0
casos = 0

while w1 != 0 and w2 != 0 and r != 0:
    valores = input().split(" ")
    w1 = float(valores[0])
    w2 = float(valores[1])
    r = float(valores[2])

    if (w1 >= 1 and w1 <= 60) and (w2 >= 1 and w2 <= 100) and (r >= 1 and r <= 12):
        rm1 = w1*(1+(r/30))
        rm2 = w2*(1+(r/30))
        m = (rm1 + rm2) / 2
        medias += m
        if m >= 1 and m < 13:
            print("Nao vai da nao")
        elif m >= 13 and m < 14:
            print("E 13")
        elif m >= 14 and m < 40:
            print("Bora, hora do show! BIIR!")
        elif m >= 40 and m <=60:
            print("Ta saindo da jaula o monstro!")
        elif m > 60:
            print("AQUI E BODYBUILDER!!")
        casos += 1
if medias/casos > 40:
    print("\nAqui nois constroi fibra rapaz! Nao e agua com musculo!")

