lista = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    
    if len(lista) == 0:
        lista.append(valor)
        print('Adicionado na ultima posição posição')
        
    else:
        pos = 0
        
        while pos < len(lista) and lista[pos] < valor:
            pos += 1
        lista.insert(pos,valor)
        
        if pos == 0:
            print(f'adicionado na posição {pos}')
            
        elif pos == len(lista) -1:
            print(f'Adicionado na posição {pos}')
            
        else:
            print(f'Adicionado na posição {pos}')
            
print(f'Os valores digitados em ordem foram : {lista}')