dados = []
pessoas = []
contpe = maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    contpe += 1
    if contpe == 1:
        maior = peso
        menor = peso  
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso       
    dados.append(nome)
    dados.append(peso)     
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().capitalize()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().capitalize()
    if continuar == 'N':
        break
print('='*30)
print(f'Foram cadastradas {contpe} pessoas.')
print(f'Nome das pessoas mais pesadas com {maior:.2f}Kg:',end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0],end= ' ')    
print(f'\nNome da pessoas mais leves com {menor:.2f}kg:',end= ' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0],end=' ')