from random import choice
from time import sleep
print('\033[1;35mJokenpô')
jogar = str(input('Você quer jogar Jokenpô contra o computador?\nSim ou Não : \033[0m')).strip().capitalize()
if jogar == 'Sim':
    lista = ['Pedra', 'Papel', 'Tesoura']
    jogador = str(input('escolha:\nPedra\nPapel\nTesoura\nSua jogada: ')).strip().capitalize()
    print('\033[1;33mJo')
    sleep(0.5)
    print('\033[1;33mKen')
    sleep(0.5)
    print('Po!!!\033[0m')
    sleep(0.5)
    computador = choice(lista)
    if jogador == 'Papel' and computador == 'Papel':
        print('Você \033[1;33mEMPATOU!\033[0m Ambos escolheram papel')
    elif jogador == 'Papel' and computador == 'Pedra':
        print('Você \033[1;32mGANHOU!\033[0m Você escolheu Papel e o computador Pedra.')
    elif jogador == 'Papel' and computador == 'Tesoura':
        print('Você \033[1;31mPERDEU!\033[0m Você escolheu Papel e o computador Tesoura.')
    elif jogador == 'Tesoura' and computador == 'Tesoura':
        print('Você \033[1;33mEMPATOU!\033[0m Ambos escolheram Tesoura.')
    elif jogador == 'Tesoura' and computador == 'Papel':
        print('Você \033[1;32GANHOU!\033[0m Você escolheu Tesoura e o computador Papel.')
    elif jogador == 'Tesoura' and computador == 'Pedra':
        print('Você \033[1;31mPERDEU!\033[0m Você escolheu Tesoura e o computador Pedra.')
    elif jogador == 'Pedra' and computador == 'Pedra':
        print('Você \033[1;33mEMPATOU!\033[0m Ambos escolheram Pedra.')
    elif jogador == 'Pedra' and computador == 'Tesoura':
        print('Você \033[1;32mGANHOU!\033[0m você escolheu Pedra e o computador Tesoura')
    elif jogador == 'Pedra' and computador == 'Papel':
        print('Você \033[1;31mPERDEU!\033[0m Você escolheu Pedra e o computador Papel.')                       
    elif jogador != 'Pedra' and jogador != 'Papel' and jogador != 'Tesoura':
        print('\033[1;31mJogada Invalida, Tente novamente!\033[0m')
else:
    print('\033[1;31mVocê é chato\033[0m')
print('\033[1;36mObrigado por Jogar\033[0m\033[1;31m❤\033[0m')