from random import choice
print('=' * 2,'sorteador', '=' * 2)
aluno = input('nome do aluno: ')
aluno2 = input('segundo aluno: ')
aluno3 = input('terceiro aluno: ')
aluno4 = input('quarto aluno: ')
lista = [aluno, aluno2, aluno3, aluno4]
print(f'sorteado foi: {choice(lista)}')