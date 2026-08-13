matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
for l in range(3):
    for c in range(3):
        print(f'[ {matriz[l][c]:^5} ]',end='')
    print()
'''valores = []
nume = []
cont = n = 0
while True:
    num = int(input(f'Digite um valor para [{cont},{n}]: '))
    nume.append(num)
    n += 1
    if n == 3:
        valores.append(nume[:])
        nume.clear()
        n = 0
        cont += 1
    if cont == 3:
        break
print('='*30)
for num in valores:
    for linha in num:
        print(f'[ {linha:^5} ]',end='')
    print()'''
