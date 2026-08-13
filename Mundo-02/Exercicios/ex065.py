c = 'S'
media = maior = menor = cont = 0
while c not in 'Nn':
    num = int(input('Digite um valor: '))
    c = str(input('Você quer continuar? [S/N] ')).strip()[0]
    cont += 1
    media += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if menor > num:
            menor = num
media = media / cont
print(f'''Você digitou {cont} números
O maior entre eles foi {maior}
O menor entre eles foi {menor}
E a média entre os números foi {media:.2f}''')