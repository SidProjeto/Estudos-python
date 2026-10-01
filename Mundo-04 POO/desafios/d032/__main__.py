from rich import print, inspect
from banco import *


def main():
    cc = ContaBancaria(123, "Gustavo", 1000)
    cc.nome = 'osvaldo'
    inspect(cc, private=True, methods=True)


if __name__ == "__main__":
    main()
