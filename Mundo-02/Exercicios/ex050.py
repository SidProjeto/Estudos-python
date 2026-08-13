print('desafio')
c = 0
f = 0
for i in range(1,7):
    num = int(input('Digite um valor: '))   
    if num % 2 == 0:
       c += num
       f += 1
print(f'Você colocou {f} números pares e sua soma foi {c}')