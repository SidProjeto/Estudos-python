n = cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    cont += 1
    if n == 999:
        break
    soma += n
print(soma,cont)