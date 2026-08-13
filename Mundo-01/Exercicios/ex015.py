d = int(input('Digite a quantidade de dias que alugara o automóvel: '))
c = float(input('Digite quantidade percorrida em Km: '))
a = d * 60
k = c * 0.15
print(f'Você tera que pagar R${a + k:.2f}')
