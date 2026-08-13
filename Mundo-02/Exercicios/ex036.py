print('\033[1;33m''Emprestimo Bancário''\033[0m')
valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Digite quantos anos vai pagar: '))
mensal = valor_casa // (anos * 12) 
limite = salario * 0.30
if  mensal > limite:
    print('\033[1;31m''Empréstimo negado!''\033[0m Excedeu 30% de seu salario')
elif mensal <= limite:
    print('\033[1;32m''Empréstmo aceito!''\033[0m')
    print(f'Você pagará R${mensal:.2f} por mês durante {anos} anos')
print('\033[1;33m''Obrigado por usar nossos serviços!''\033[0m')