from class031 import *
from rich import print, inspect


def main():
    r = Retangulo()
    try:
        r.base = 2
        r.altura = 3
        r.medidas = (3, 4)

    except Exception as e:
        print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")

    print(r.medidas)


if __name__ == "__main__":
    main()
