from random import randint
from time import sleep


def sorteio(lista):
    print("sorteando 5 valores da lista:", end=" ", flush=True)
    for cont in range(5):
        valor = randint(1, 10)
        sleep(0.5)
        print(valor, end=" ", flush=True)
        lista.append(valor)
    print("PRONTO!")


def somaPar(lista):
    par = 0
    for valor in lista:
        if valor % 2 == 0:
            par += valor
    print(f"Somando os valores pares de {lista} temos {par}")


numeros = []

sorteio(numeros)
somaPar(numeros)
