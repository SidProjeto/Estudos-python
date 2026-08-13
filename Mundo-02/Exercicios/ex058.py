from random import randint
from time import sleep
print(f'''\033[1;33m{ '≈' * 53}
Tente Acertar o número que o Pc Está pensando. 1 a 10
{'≈' * 53}\033[0m
''')
cont = 0
pc = randint(1,10) #sorteia um número aleatório entre 1 e 10
acertou = False
while not acertou: #loop, so acaba caso não for 'S' ou 's'
    jogador = int(input('escreva um número: '))
    cont += 1
    print('\033[1;35mComputador está pensando...\033[m')
    sleep(1)
    if jogador == pc: # se for igual, então jogador vence
        print('\033[1;32mvocê acertou!\033[m')
        acertou = True
    else: # caso o if de cima não for verdadeiro retorna isso
        if pc > jogador:
            print('Mais pra cima')
        elif pc < jogador:
            print('Mais pra baixo')    
print(f'''Obrigado por jogar!
Você jogou {cont} vez(es) para vencer.''')