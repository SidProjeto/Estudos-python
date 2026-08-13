lista = []
pilha = []
expressao = str(input('Digite a expressão: '))
lista.append(expressao)
for valor in expressao:
    if valor == '(':
        pilha.append('(')
    elif valor == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
print('='*30)

if len(pilha) == 0:
    print('A expressão:',end=' ')
    for l in lista:
        print(f'{l} é valida\n')
else:
    print('A expressão',end=' ')
    for l in lista:
        print(f'{l} é invalida\n')
        
        