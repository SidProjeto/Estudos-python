info = []
somaidades = 0

while True:

    dados = {}
    dados["Nome"] = str(input("Nome: ")).strip().capitalize()
    dados["Sexo"] = str(input("Sexo [M/F]: ")).strip().upper()

    while dados["Sexo"] not in "MF":
        dados["Sexo"] = str(input("Sexo [M/F]: ")).strip().upper()

    dados["Idade"] = int(input("Idade: "))
    somaidades += dados["Idade"]

    info.append(dados.copy())
    del dados

    resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()

    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()

    if resp == "N":
        break

print("-=" * 30)
media = somaidades / len(info)
print(f"- Foi cadastrado {len(info)} pessoas")
print(f"- A média de idade das pessoas é {media:.2f} anos.")

print("- As mulheres são: ", end="")
for c in info:
    if c["Sexo"] == "F":
        print(c["Nome"], end="; ")

print("\n- Lista das pessoas acima da média de idade: ")
print()

for c in info:
    if c["Idade"] > media:
        print(f"Nome: {c['Nome']}; Idade: {c['Idade']}; Sexo: {c['Sexo']};")
        print()
        
print("<< ENCERRADO >>")
