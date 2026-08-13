from random import randint
from time import sleep
computador = '' 
escolha = vitoria = 0
while True:
    jogador = str(input('Escolha Par ou Impar: ')).strip().capitalize()
    if jogador not in 'ParImpar':
        jogador = str(input('Invalido! Escolha novamente. ')).strip().capitalize()
    escolha += 1
    if escolha == 1:
        if jogador == 'Par':
            computador == 'Impar'
        else:
            computador == 'Par'
    jogador_jogada = int(input('Faça sua jogada: '))
    print('Computador esta pensando...')
    sleep(1)
    print('Computador fez sua jogada!')
    sleep(0.5)
    computador_jogada = randint(0,10)
    soma = jogador_jogada + computador_jogada
    if soma % 2 == 0:
        if jogador == 'Par':
            print(f'O número {soma} é par, você venceu!')
            vitoria += 1
            continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()
            if continuar in 'Ss':
                continuar = ''
            else:
                break
        else:
            print(f'O número {soma} é par, Você perdeu!')
            break
    else:
        if jogador == 'Impar':
            print(f'O número {soma} é impar, você venceu!')
            vitoria += 1
            continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()
            if continuar in 'Ss':
                continuar = ''
            else:
                break
        else:
            print(f'O número {soma} é impar, você perdeu!')
            break
sleep(0.5)
print(f'''Obrigado por jogar
você venceu {vitoria} vezes consecutivas!''')