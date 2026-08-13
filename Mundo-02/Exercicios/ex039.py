from datetime import date
print('\033[1;33m''Alistamento Militar Obrigatorio''\033[0m')
ano = int(input('Em qual ano você nasceu? '))
data = date.today().year
genero = str(input('Qual é seu Gênero, Masculino ou Feminino: ')).capitalize()
if  genero == 'Feminino':
    print('Você não é obrigada a se alistar!')
elif data - ano < 18:
    print(f'você ainda vai se alistar, Falta {18 -(data - ano)} ano!')
elif data - ano > 18:
    print(f'Já passou do tempo de se alistar,\npassou-se {data - ano - 18} ano')
elif data - ano == 18:
    print('Você tem 18 anos, é a hora de se alistar')
