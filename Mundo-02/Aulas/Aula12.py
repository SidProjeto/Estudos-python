nome = str(input('Qual é seu nome: ')).capitalize()
if nome == 'Gustavo':
    print(f'Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome == 'Julia' or nome == 'Sofia' or nome == 'Isabella':
    print('Que belo nome feminino')
print(f'Tenha um bom dia, {nome}!')
