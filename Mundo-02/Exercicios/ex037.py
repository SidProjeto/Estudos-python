from time import sleep
print('\033[1;33m''Base de conversão''\033[0m')
num = int(input('Coloque um valor: '))
selecao = str(input('\033[1;33m''1 para binário\n2 para octal\n3 para hexadecimal\nSua opção: \033[0m'))
if selecao == '1':
    bi = bin(num)
    print('\033[1;36m''Convertendo para Binário...''\033[0m')
    sleep(3)
    print(f'O número {num} convertido é {bi[2:]}')
elif selecao == '2':
    oc = oct(num)
    print('\033[1;36m''Convertendo para Octal...''\033[0m')
    sleep(3)
    print(f'O número {num} convertido é {oc[2:]}')
elif selecao == '3':
    hexa = hex(num)
    print('\033[1;36m''Convertendo para Hexadecimal...''\033[0m')
    sleep(3)
    print(f'O número {num} convertendo é {hexa[2:]}')
else:
    print('Opção Invalida! Tente novamente')