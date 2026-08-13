lista = []
while True:
    valor = int(input('Digite um valor: '))
    
    if valor in lista:
        print('Valor ja foi inserido! não sera considerado.')
        
    else:
        lista.append(valor)
        print('Valor foi adicionado com sucesso!')
            
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('invalido! tente novamente: ')).strip().upper()
        
    if continuar == 'N':
        break
    
lista.sort()          
print(f'Você digitou: {lista}')