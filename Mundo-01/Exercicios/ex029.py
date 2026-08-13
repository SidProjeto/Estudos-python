vel = int(input('Qual foi sua velocidade? km:'))
if vel > 80:
    print('Foi multado por ter excedido a velocidade de 80km/h!')
    print(f'Terá que pagar uma multa de R${float(7 * (vel - 80)):.2f}')
print('Tenha um bom dia! Dirija com segurança!')