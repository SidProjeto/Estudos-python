num = int(input('Digite um número: '))
decisao = num % 2
if decisao == 1:
    print(f'{num} é impar')
else:
    print(f'{num} é par')