from time import sleep
num = float(input('Digite um valor '))
num2 = float(input('Outro valor '))
escolha = 0
while escolha != 5:
    print(f'''\033[1;33m========= Menu =========
[1] Somar
[2] Multiplicar
[3] Maior
[4] novos números
[5] sair do programa
{'=' * 24}\033[m''')
    escolha = int(input('Sua opção: '))
    if escolha == 1:
        print(f'{num} + {num2} = {num + num2}')
    elif escolha == 2:
        print(f'{num} x {num2} = {num * num2}')
    elif escolha == 3:
        print(f'O maior número entre eles é {max(num,num2):.1f}')
    elif escolha == 4:
        num = float(input('Digite um valor: '))
        num2 = float(input('Outro valor: '))
    elif escolha == 5:
        print('fechando...')
        sleep(1)
    else:
        print('Opção invalida. Tente novamente!')
    sleep(1)
print('obrigado por usar')