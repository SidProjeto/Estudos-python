info = []
while True:
    dados = []
    nome = str(input('Nome: ')).strip().capitalize()
    dados.append(nome)
    
    for c in range(2):
        nota = float(input(f'Nota {c+1}: '))
        dados.append(nota)
        
    info.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().capitalize()
    
    while continuar not in 'SN':
        continuar = str(input('Dado invalido! Digite [S/N]: ')).strip().capitalize()
        
    if continuar == 'N':
        break
    
print(f'{'='*5} {'BOLETIM':^10} {'='*5}')
print(f'{'Id':<3} {'NOME':<10}{'MÉDIA':>6}')
print('='*22)

for p,c in enumerate(info):
    print(f'{p:<3} {c[0]:<10}',end=' ')
    
    notas = c[1:]
    media = sum(notas)/ len(notas)
    
    print(f'{media:>6.1f}')
print('='*40)

while True:
    id = int(input('Digite o id do aluno para ver as notas (-1 interrompe): '))
    
    if id == -1:
        break
    
    if 0 <= id < len(info):
        print('='*40)
        print(f'Notas do {info[id][0]}:',end=' ')
        
        for notas in info[id][1:]:
            print(notas,end=' ')
        print(f'\n{'='*40}')
        
    else:
        print('Id invalido')
        