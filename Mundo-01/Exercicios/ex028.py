from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. tente adivinhar...')
print('-=-' * 20)
num = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(3)
random = randint(0,5)
if num == random:
    print('Parábens! você me venceu!')
else:
    print(f'Você perdeu! Eu pensei em {random} e não no {num}')
