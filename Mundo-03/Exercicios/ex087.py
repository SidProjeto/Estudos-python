matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = soma3 = cont = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite valor para [{l},{c}]: '))
for l in range(3):
    for c in range(3):
        print(f'[ {matriz[l][c]:^5} ]',end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
for l in matriz:
    for c in l:
        cont += 1
        if cont == 3:
            soma3 += c
            cont = 0
for l in matriz[1]:
    if cont == 0:
        maior = l
    else:
        if maior < l:
            maior = l
print(f'A soma de todos os valores pares digitados é {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')
'''valores = []
nume = []
cont = n = soma = soma3 = maior = 0
while True:
    num = int(input(f'Digite um valor para [ {cont},{n} ]: '))
    n += 1
    nume.append(num)
    if n == 3:
        valores.append(nume[:])
        nume.clear()
        n = 0
        cont += 1
    if cont == 3:
        break
print('-='*30)
for linhas in valores:
    for num in linhas:
        print(f'[ {num} ]',end=' ')
    print()
for linhas in valores:
    c = 1
    for numeros in linhas:

        if numeros % 2 == 0:
            soma +=  numeros
        if c == 3:
            soma3 += numeros
            c = 1
        c += 1
print(f'A soma da lista é {soma}')
print(f'A soma dos valores da terceira linha é {soma3}')
for linhas in valores[1]:
    c = 0
    if c == 0:
        maior = linhas
    else:
        if linhas > maior:
            maior = linhas
    c += 1
print(f'O maior valor da segunda linha é {maior}')'''