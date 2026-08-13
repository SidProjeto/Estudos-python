print('Calculador de pagamento à vista com desconto de 10%\n e parcelado com aumento de 8%')
v = float(input('Digite o valor atual: '))
print(f'À vista fica: R${v - (v * (10 / 100)):.2f}\nParcelando fica: R${v + (v * (8 / 100)):.2f}')

