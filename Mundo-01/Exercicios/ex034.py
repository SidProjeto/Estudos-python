salario = float(input('Digite seu salário R$'))
if salario <= 1250:
    print(f'Vai ter um aumento de 15%, ficando R${salario +(salario * 15/100):.2f}')
else:
    print(f'Vai ter um aumento de 10%, ficando R${salario +(salario * 10/100):.2f}')
