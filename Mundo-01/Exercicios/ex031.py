print('Calculador de preço de passagem de ônibus')
distancia = float(input('Quanto você percorreu? KM:'))
preco = 0.50
preco2 = 0.45
if distancia <= 200:
    print(f'preço da passagem será R${(distancia * preco):.2f}')
else:
    print(f'preço da passagem será R${(distancia * preco2):.2f}')