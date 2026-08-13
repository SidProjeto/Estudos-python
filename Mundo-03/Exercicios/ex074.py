from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('A listagem é: ', end='')
for i in tupla:
    print(i, end=' ')
print(f'''\nO maior número é {max(tupla)} 
O menor número é {min(tupla)}''')
