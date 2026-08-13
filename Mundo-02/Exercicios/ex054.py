from datetime import date
print('maioridade')
maiores = 0
menores = 0
data_atual = date.today().year
for i in range(7):
    ano = int(input('Em qual ano você nasceu? '))
    if data_atual - ano >= 18:
        maiores += 1
    else:
        menores += 1
print(
f'''pessoas maiores ou de 18 anos: {maiores}
pessoas menores de 18 anos: {menores}''')