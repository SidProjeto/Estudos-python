print(f'''{'='*26}
  CAIXA ELETRÔNICO 24HRS
{'='*26}''')
resto = 0
while True:
    saque = int(input('Quanto deseja sacar? R$'))
    resto = saque
    if saque // 50 >= 1:
        nota50 = resto // 50
        resto %= 50
        print(f'total de {nota50} cédulas de R$50')
    if resto // 20 >= 1:
        nota20 = resto // 20
        resto %= 20
        print(f'total de {nota20} cédulas de R$20')
    if resto // 10 >= 1:
        nota10 = resto // 10
        resto %= 10
        print(f'total de {nota10} cédulas de R$10')
    if resto // 1 >= 1:
        nota1 = resto // 1
        print(f'total de {nota1} cédulas de R$1')
    print(f'{'='*26}')
    break