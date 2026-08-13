cont = num = num0 = num1 = num2 = num3 = 0
for i in range(4):
    cont += 1
    num = int(input('Digite um valor: '))
    if cont == 1:
        num0 = num
    elif cont == 2:
        num1 = num
    elif cont == 3:
        num2 = num
    elif cont == 4:
        num3 = num
    tupla = (num0,num1,num2,num3)
print(f'''Você digitou os valores {tupla}
O número 9 apareceu: {tupla.count(9)} vezes''')
if 3 in tupla:
    print(f'O primeiro número 3 apareceu na {tupla.index(3)+ 1}º posição')
else:
    print('O número 3 não foi digitado')
print('O números pares foram: ', end= '')
for i in range(0,4):
    if tupla[i] % 2 == 0:
            print(tupla[i],end=' ')