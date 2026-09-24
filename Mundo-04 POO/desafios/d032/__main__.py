from rich import print, inspect
from banco import *


def main():
    cc = ContaBancaria(123, "Gustavo", 1000, 123)
    cc.sacar(100, 123)
    print(cc.saldo)
    inspect(cc, private=True, methods=True)


if __name__ == "__main__":
    main()
