'''lanche = ('Hambúguer','Suco','Pizza','Pudim','Batata frita')# Tuplas são imutaveis

for comida in lanche:
    print(f'Eu vou comer {comida} ')
    
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
    
for pos, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche)) Ordenado
print('comi pra caramba!')'''

'''a = (2,5,4)
b = (5,8,1,2)
c = a + b # c = b + a é diferente
print(c.count(5))  conta quanta vezes aparece
print(c.index(5)) mostra em qual posição está o número'''

'''pessoa = ('Gustavo',39,'M',99.88)
del(pessoa) deleta a tupla
print(pessoa)'''