listagem = (('Lápis', 1.75),('Borracha', 2),('Caderno', 15),('Estojo',25),('Transferido',
            4.20),('Compasso',9.99),('Mochila', 120.32),('Caneta',22.30),('Livro',34.90))
print(f'''{'-'*30}
{'Listagem de preços':^30}
{'-'*30}''')
for nome, preco in listagem:
    print(f'{nome:.<20}R$ ', end=' ')
    print(f'{preco:>6.2f}')
print(f'-'*30)