lista_par = [] 
lista_impar = []
lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().capitalize()
    
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().capitalize()
        
    if continuar == 'N':
        break
    
for valor in lista:
    
    if valor % 2 == 0:
        lista_par.append(valor)
        
    else:
        lista_impar.append(valor)
        
print(f'''A lista completa é {lista}
A lista de pares é {lista_par}
A lista de ímpares é {lista_impar}''')