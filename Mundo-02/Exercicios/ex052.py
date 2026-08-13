print('Número primo')
num = int(input('Digite um número: '))
raiz = int(num**0.5)
primo = 0
if num < 2:
    print('não é primo')
elif num == 2:
    print('sim é primo')
else:
    for i in range(2, raiz + 1):
        if num % i == 0:
            primo += 1
if primo == 0:
    print('sim é primo')
else:
    print('não é primo')
