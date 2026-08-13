lista = []
continuar = ''
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().capitalize()
    
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().capitalize()
        
    if continuar == 'N':
        break
    
lista.sort(reverse=True)
print(f'''Foi digitado {len(lista)} números
Lista ordenada de forma descrescente: {lista}''')

if 5 in lista:
    print('O número 5 está nas posições:', end= ' ')
    
    for pos, valor in enumerate(lista):
        
        if valor == 5:
            print(f'{pos + 1}',end=' ')
else:
    print('O número 5 não está na lista')