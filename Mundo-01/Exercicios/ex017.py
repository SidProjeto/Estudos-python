from math import hypot
print('Calculador de Pitágoras')
n = float(input('Valor do cateto oposto: '))
n2 = float(input('Valor do cateto adjacente: '))
h = hypot(n, n2)
print(f'Valor da hipótenusa é {h:.2f}')