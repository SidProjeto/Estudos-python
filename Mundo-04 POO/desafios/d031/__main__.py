from class031 import *
from rich import print, inspect


def main():
    r = Retangulo()
    r.altura = 33
    r.base = 23
    r.medidas = (9, 3)
    inspect(r, private=True, methods=True)
    print(r.medidas)


if __name__ == "__main__":
    main()
