print('\033[1;33m''Qual é o maior''\033[0m')
num = int(input('Digite um valor: '))
num2 = int(input('Outro valor: '))
if num > num2:
    print(f'O {num} é maior!')
elif num2 > num:
    print(f'O {num2} é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')