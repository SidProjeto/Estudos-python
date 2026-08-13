'''num = [2,5,9,1]
num[2] = 3
num.append(7) adiciona na lista
num.sort(reverse=True) apenas o sort, ele organiza crescente, com reverse=True dentro descrescente
num.insert(2,2) adiciona na lista no indice pedido
num.pop() sem nada dentro remove o ultimo indice junto de seu valor, com um indice dentro remove o valor escolhido
num.remove(4) remove o valor procurado
'''
'''valores = list()
for cont in range(5):
    valores.append(int(input('Digite um valor: ')))

for c,v in enumerate(valores):
    print(f'\nna posição {c} encontrei o valor {v}',end= ' ')
'''
'''a = [2,3,4,7]
b = a[:] cria uma copia da lista a, se for apenas 'b = a' ele cria uma ligação entre as listas
b[2] = 8
b.remove()
print(f'lista A: {a}')
print(f'lista b: {b}')'''
lista = [1,2,3,4,5]
lista.insert(5,2)
print(lista)