cont_f_menor = cont_m = cont_idade = cont_f = 0
while True:
    print(f'''{'=' * 20}
CADASTRE UMA PESSOA
{'=' *20}''')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print('=' * 20)
    if idade >= 18:
        cont_idade += 1
    if sexo in 'F' and idade < 20:
        cont_f_menor += 1
    if sexo in 'M':
        cont_m += 1
    else:
        cont_f += 1
    continuar = ' '
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'''Pessoas maiores de 18: {cont_idade}
Total de Homens cadastrados: {cont_m}
Mulheres menores de 20: {cont_f_menor}''')