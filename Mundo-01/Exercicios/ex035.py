l1 = float(input('Digite um comprimento: '))
l2 = float(input('Outro comprimento: '))
l3 = float(input('Outro comprimento: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')