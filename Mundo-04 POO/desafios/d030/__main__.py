from class030 import *
from rich import print, inspect


def main():
    c = Credencial()
    c.senha = "agua"
    inspect(c, private=True, methods=True)
    print(c.validar("agu"))


if __name__ == "__main__":
    main()
