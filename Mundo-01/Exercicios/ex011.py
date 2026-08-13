print('Calculador de área e quantidade\nde tinta necessária para uma parede')
l = float(input('coloque a largura em metros: '))
al = float(input('coloque a altura em metros: '))
t = 2
a = l * al
n = a / 2
print(f'A sua área é {a:.2f}m²\n a quantidade de tinta necessária é {n:.2f}l')
