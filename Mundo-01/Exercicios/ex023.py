num = int(input('Digite um valor de 0 a 9999: '))
print(f'unidade: {num // 1 % 10}\ndezena: {num // 10 % 10}\ncentena: {num // 100 % 10}\nmilhar: {num // 1000 % 10}')
