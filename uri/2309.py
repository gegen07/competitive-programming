numPartidas = int(input())

contPartidasA = 0
contPartidasB = 0

cartas = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]

for i in range(numPartidas):
	cards = [int(j) for j in input().split()]

	cartasA = 0
	cartasB = 0

	for k in range(3):
		if cartas.index(cards[k]) >= cartas.index(cards[k+3]):
			cartasA += 1
		else:
			cartasB += 1

	if cartasA > cartasB:
		contPartidasA += 1
	else:
		contPartidasB += 1

print(contPartidasA, contPartidasB)