dados = {}
dados["nome"] = str(input("Nome: ")).strip().capitalize()
dados["media"] = float(input(f"Media de {dados["nome"]}: "))
print("=" * 30)

if dados["media"] >= 7:
    dados["situacao"] = "Aprovado"

elif dados["media"] < 5:
    dados["situacao"] = "Reprovado"

else:
    dados["situacao"] = "Recuperação"

for i,v in dados.items():
    print(f"{i} é igual a {v}")