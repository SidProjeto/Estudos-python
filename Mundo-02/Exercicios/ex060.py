print('Fatorial')
num = int(input('Digite um valor: '))
ft = 1
cont = num
print(f'{num}! = ' , end='')
while cont > 1:
    print(cont, end='')
    if cont > 1:
        ft *= cont
        print( ' x ', end='')
    cont -= 1
print(f'{ft}')
'''num = int(input('Digite um valor: '))
ft = 1
i = 0
print(f'{num}!')
for i in range(num, 0, -1):
    print(i, end='')
    print(' x ' if i > 1 else ' = ', end='')
    ft *= i
print(ft)'''