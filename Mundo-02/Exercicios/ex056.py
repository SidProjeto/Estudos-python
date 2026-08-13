print('Desafio')
idade_atual = 0
idade_media = 0
cont = 0
soma_idade = 0
nome_v = ''
for i in range(1,6):
    print(f'---- {i}ª Pessoa ----')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M' and idade > idade_atual:
        idade_atual = idade
        nome_v = nome       
    soma_idade += idade
    if sexo == 'F' and idade < 20:
        cont += 1
idade_media = soma_idade / 4
print(
f'''Nome do homem mais velho: {nome_v}
A média da idade do grupo: {idade_media:.2f}
Mulheres menores de 20 anos: {cont}''')