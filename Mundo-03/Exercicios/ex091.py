from random import randint
from time import sleep
from operator import itemgetter

cont = 1
rpg = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
}

print("Valores sorteados:")
for j, d in rpg.items():
    sleep(1)
    print(f" O {j} rolou um dado e caiu {d}")

ranking = dict(sorted(rpg.items(), key=itemgetter(1), reverse=True))
print("Ranking dos jogadores:")

for v, c in ranking.items():
    sleep(1)
    print(f" O {cont}º lugar: {v} com {c}", end=" ")
    print()
    cont += 1
