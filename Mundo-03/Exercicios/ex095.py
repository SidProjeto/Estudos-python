carreira = {}
gols = []
info = []

while True:

    print("-" * 30)
    carreira["nome"] = str(input("Nome: ")).strip().capitalize()
    partidas = int(input("Jogou quantas partidas? "))

    for i in range(partidas):
        gols.append(int(input(f"Quantos gols marcados na {i + 1}º partida? ")))

    resp = str(input("quer continuar? [S/N] ")).strip().upper()
    while resp not in "SN":
        resp = str(input("quer continuar? [S/N] ")).strip().upper()

    carreira["gols"] = gols[:]
    carreira["totgols"] = sum(gols)
    info.append(carreira.copy())
    carreira.clear()
    gols.clear()

    if resp == "N":
        break

print("-=" * 30)
print(f"{'id':<3} {'nome':<10} {'gols':<20} {'total':<30}")
print("-" * 50)

for i, v in enumerate(info):
    print(f"{i:<3} {v['nome']:<10} {str(v['gols']):<20} {v['totgols']:<30}")
print("-" * 50)

while True:

    opcao = int(input("Mostrar dados de qual jogador? "))

    if opcao < 0:
        break
    if opcao >= len(info):

        print(f"ERRO, não exite jogador com o id {opcao}! Tente novamente")

    else:
        print("-" * 30)
        print(f"-- Dados do JOGADOR {info[opcao]['nome']}")

        for i, c in enumerate(info[opcao]["gols"]):
            print(f"  No jogo {i + 1} fez {c} gols")
        print("-" * 30)

print("<< VOLTE SEMPRE >>")
