from random import shuffle
print('=' * 2,'Sorteador de apresentação', '=' * 2)
aluno = input('nome do aluno: ')
aluno2 = input('segundo aluno: ')
aluno3 = input('terceiro aluno: ')
aluno4 = input('quarto aluno: ')
lista = [aluno, aluno2, aluno3, aluno4]
shuffle(lista)
print(f'A ordem sorteada foi\n{lista[0]}\n{lista[1]}\n{lista[2]}\n{lista[3]}')