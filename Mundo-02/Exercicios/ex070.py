compra_total = produtos_1000 = barato_preco = cont = 0
barato_nome = ''
print(f'''{'=' *20}
    SUPERMARKET
{'='*20}''')
while True:
    nome_produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('O preço do Produto: R$'))
    cont += 1
    if cont == 1:
        barato_nome = nome_produto
        barato_preco = preco
    if preco < barato_preco:
        barato_nome = nome_produto
        barato_preco = preco
    if preco >= 1000:
        produtos_1000 += 1
    compra_total += preco
    continuar = ' '
    while continuar != 'S' and continuar != 'N':
         continuar = str(input('Você deseja continuar? [S/N] ')).strip().capitalize()
    if continuar in 'N':
            break 
print(f'''{'='*13} FIM DO PROGRAMA {'='*13}
O Produto mais barato é {barato_nome} custando R${barato_preco:.2f}
{produtos_1000} Produtos comprados acima de R$1000,00
A compra total foi de: R${compra_total:.2f}''')      