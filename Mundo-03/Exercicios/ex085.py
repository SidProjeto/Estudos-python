valores = [[],[]]
for c in range(7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'''Os valores pares digitados foram: {valores[0]}
Os valores impares digitados foram: {valores[1]}''')
