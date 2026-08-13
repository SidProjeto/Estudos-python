num = 1
limite = int(input('Você quer ver Quantos termos? '))
soma = 0
num2 = 0
num3 = 0
cont = 0
while limite != 0:
    print(soma, end='->')
    soma = num + (num2) #1
    num3 = num
    num = soma
    cont += 1
    if num2 >= 0 and cont >= 2:
        num2 = num3
    if cont == limite:
        limite = 0
print('acabou')