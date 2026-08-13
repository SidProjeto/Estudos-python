carreira = {}
gols = []

carreira["nome"] = str(input("Nome: ")).strip().capitalize()
partidas = int(input("Jogou quantas partidas? "))

for i in range(partidas):
    gols.append(int(input(f"Quantos gols marcados na {i + 1}º partida? ")))

carreira["gols"] = gols[:]
carreira["totgols"] = sum(gols)

print("-=" * 30)
print(carreira)
print("-=" * 30)

for i, v in carreira.items():
    print(f"O campo {i} tem o valor {v}")

print("-=" * 30)
print(f"O jogador {carreira['nome']} jogou {partidas} partidas")

for c, i in enumerate(carreira["gols"]):
    print(f"   => Na partida {c + 1}, fez {i} gols")
print(f"fez um total de {carreira['totgols']} gols")
