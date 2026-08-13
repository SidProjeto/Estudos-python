from random import randint
from time import sleep
jogo = []
print(f'''{'='*30}
{'MEGA SENA':^30}
{'='*30}''')
sorteio = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{'='*5} SORTEANDO {sorteio} JOGOS {'='*5}')
for n in range(sorteio):
    nume = []
    while len(nume) < 6:
        num = randint(1,60)
        if num not in nume:
            nume.append(num)
    jogo.append(nume[:])
    nume.clear()
for n in range(sorteio):
    jogo[n].sort()
    print(f'Jogo{n + 1}: {jogo[n]}')
    sleep(0.5)
print(f'{'='*12} BOA SORTE {'='*12}')