primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 1
total = 0
limite = 10
while cont <= limite:
    print(primeiro , end='->')
    print(' PAUSA' if cont == limite else '', end='')
    primeiro += razao
    cont += 1
    total += 1
    if cont > limite:
        escolha = int(input('\nquanto termos você quer mostrar a mais? '))
        if escolha > 0:
            limite = escolha
            cont = 1
print(f'foi mostrado {total} termos')