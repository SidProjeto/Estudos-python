print('\033[1;33m10 termos de uma PA\033[0m')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razão: '))
for i in range(1, 11):
    print(primeiro, end=' ->')
    primeiro += razao
print('Acabou!')   