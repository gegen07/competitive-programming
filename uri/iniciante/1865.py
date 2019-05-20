numTentados = int(input())

for i in range(numTentados):
    tentado = input().split(" ")
    nome, forca = tentado
    if nome == "Thor":
        print("Y")
    else: 
        print("N")