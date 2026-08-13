num = cont = soma = 0
num = int(input('Digite um valor: '))
while num != 999: 
    soma += num
    cont += 1
    num = int(input('Digite um valor: '))
print(f'''Foi digitado {cont} números
e a soma entre eles foi {soma}''')