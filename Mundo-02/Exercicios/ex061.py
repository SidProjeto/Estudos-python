primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    cont += 1
    print(primeiro, end='->')
    primeiro += razao
print('Acabou')