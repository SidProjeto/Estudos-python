from datetime import date

dados = {}
dados["nome"] = str(input("Nome: ")).strip().capitalize()
dados["idade"] = int(input("Ano de nascimento: "))
dados["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))

if dados["ctps"] != 0:
    dados["contratação"] = int(input("Ano de contratação: "))
    dados["salário"] = float(input("Salário R$"))
    dados["aposentadoria"] = dados["contratação"] + 35 - dados["idade"]

dados["idade"] = date.today().year - dados["idade"]
print("=" * 30)

for n, v in dados.items():
    print(f"{n} tem valor {v}")
